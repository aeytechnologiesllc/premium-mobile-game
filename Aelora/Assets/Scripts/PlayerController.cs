using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [Header("Lanes")]
    [SerializeField] private float laneWidth = 2.5f;
    [SerializeField] private float laneSwitchSpeed = 10f;
    private int currentLane = 1; // 0=left, 1=center, 2=right
    private float targetX;

    [Header("Jump")]
    [SerializeField] private float jumpForce = 12f;
    [SerializeField] private float gravity = -30f;
    [SerializeField] private float coyoteTime = 0.1f;
    private float verticalVelocity;
    private bool isGrounded = true;
    private float lastGroundedTime;

    [Header("Slide")]
    [SerializeField] private float slideDuration = 0.6f;
    [SerializeField] private float slideColliderHeight = 0.5f;
    private float slideTimer;
    private bool isSliding;
    private float normalColliderHeight;
    private Vector2 normalColliderCenter;

    [Header("Magic")]
    [SerializeField] private float magicCooldown = 2f;
    [SerializeField] private GameObject magicEffectPrefab;
    private float magicTimer;

    [Header("References")]
    [SerializeField] private BoxCollider2D playerCollider;
    [SerializeField] private Animator animator;

    private bool isDead;
    private float groundY;

    void Start()
    {
        groundY = transform.position.y;
        targetX = 0f; // center lane

        if (playerCollider != null)
        {
            normalColliderHeight = playerCollider.size.y;
            normalColliderCenter = playerCollider.offset;
        }
    }

    void OnEnable()
    {
        SwipeInput.OnSwipe += HandleSwipe;
        SwipeInput.OnTap += HandleTap;
    }

    void OnDisable()
    {
        SwipeInput.OnSwipe -= HandleSwipe;
        SwipeInput.OnTap -= HandleTap;
    }

    void Update()
    {
        if (isDead) return;

        UpdateLanePosition();
        UpdateVerticalMovement();
        UpdateSlide();
        UpdateMagicCooldown();
        UpdateAnimations();
    }

    void HandleSwipe(SwipeInput.SwipeDirection direction)
    {
        if (isDead) return;

        switch (direction)
        {
            case SwipeInput.SwipeDirection.Up:
                Jump();
                break;
            case SwipeInput.SwipeDirection.Down:
                Slide();
                break;
            case SwipeInput.SwipeDirection.Left:
                SwitchLane(-1);
                break;
            case SwipeInput.SwipeDirection.Right:
                SwitchLane(1);
                break;
        }
    }

    void HandleTap()
    {
        if (isDead) return;
        CastMagic();
    }

    void Jump()
    {
        bool canJump = isGrounded || (Time.time - lastGroundedTime < coyoteTime);
        if (!canJump) return;

        verticalVelocity = jumpForce;
        isGrounded = false;

        if (isSliding) EndSlide();
    }

    void Slide()
    {
        if (!isGrounded || isSliding) return;

        isSliding = true;
        slideTimer = slideDuration;

        if (playerCollider != null)
        {
            playerCollider.size = new Vector2(playerCollider.size.x, slideColliderHeight);
            playerCollider.offset = new Vector2(playerCollider.offset.x, slideColliderHeight / 2f);
        }
    }

    void EndSlide()
    {
        isSliding = false;

        if (playerCollider != null)
        {
            playerCollider.size = new Vector2(playerCollider.size.x, normalColliderHeight);
            playerCollider.offset = normalColliderCenter;
        }
    }

    void SwitchLane(int direction)
    {
        int newLane = currentLane + direction;
        if (newLane < 0 || newLane > 2) return;

        currentLane = newLane;
        targetX = (currentLane - 1) * laneWidth;
    }

    void CastMagic()
    {
        if (magicTimer > 0f) return;

        magicTimer = magicCooldown;

        if (magicEffectPrefab != null)
        {
            GameObject effect = Instantiate(magicEffectPrefab, transform.position, Quaternion.identity);
            Destroy(effect, 1.5f);
        }

        // Destroy nearby obstacles
        Collider2D[] hits = Physics2D.OverlapCircleAll(transform.position, 4f);
        foreach (var hit in hits)
        {
            if (hit.CompareTag("Obstacle"))
            {
                Destroy(hit.gameObject);
                GameManager.Instance?.AddScore(10);
            }
        }
    }

    void UpdateLanePosition()
    {
        Vector3 pos = transform.position;
        pos.x = Mathf.Lerp(pos.x, targetX, laneSwitchSpeed * Time.deltaTime);
        transform.position = pos;
    }

    void UpdateVerticalMovement()
    {
        if (isGrounded && verticalVelocity <= 0)
        {
            verticalVelocity = 0f;
            lastGroundedTime = Time.time;
            return;
        }

        verticalVelocity += gravity * Time.deltaTime;

        Vector3 pos = transform.position;
        pos.y += verticalVelocity * Time.deltaTime;

        if (pos.y <= groundY)
        {
            pos.y = groundY;
            verticalVelocity = 0f;
            isGrounded = true;
        }

        transform.position = pos;
    }

    void UpdateSlide()
    {
        if (!isSliding) return;

        slideTimer -= Time.deltaTime;
        if (slideTimer <= 0f) EndSlide();
    }

    void UpdateMagicCooldown()
    {
        if (magicTimer > 0f)
            magicTimer -= Time.deltaTime;
    }

    void UpdateAnimations()
    {
        if (animator == null) return;

        animator.SetBool("IsGrounded", isGrounded);
        animator.SetBool("IsSliding", isSliding);
        animator.SetFloat("VerticalVelocity", verticalVelocity);
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Obstacle"))
        {
            Die();
        }
        else if (other.CompareTag("Collectible"))
        {
            GameManager.Instance?.AddScore(1);
            Destroy(other.gameObject);
        }
        else if (other.CompareTag("CrownShard"))
        {
            GameManager.Instance?.CollectCrownShard();
            Destroy(other.gameObject);
        }
    }

    void Die()
    {
        isDead = true;
        GameManager.Instance?.GameOver();
    }
}
