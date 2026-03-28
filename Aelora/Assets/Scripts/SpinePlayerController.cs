using UnityEngine;

/// <summary>
/// Bridges the PlayerController with Spine skeleton animations.
/// Attach this to the same GameObject as PlayerController.
/// When the Spine-Unity runtime is imported, swap the placeholder
/// Animator references for SkeletonAnimation calls.
/// </summary>
public class SpinePlayerController : MonoBehaviour
{
    [Header("Animation Names")]
    private const string ANIM_IDLE = "idle";
    private const string ANIM_RUN = "run";
    private const string ANIM_JUMP = "jump";
    private const string ANIM_SLIDE = "slide";
    private const string ANIM_MAGIC = "magic";

    [Header("State")]
    private string currentAnimation = "";
    private bool isGrounded = true;
    private bool isSliding;

    // Spine reference - uncomment when Spine-Unity runtime is imported:
    // [SerializeField] private Spine.Unity.SkeletonAnimation skeletonAnimation;

    private Animator animator; // Fallback for testing without Spine

    void Start()
    {
        animator = GetComponent<Animator>();
        PlayAnimation(ANIM_RUN, true);
    }

    void OnEnable()
    {
        SwipeInput.OnSwipe += OnSwipe;
        SwipeInput.OnTap += OnTap;
    }

    void OnDisable()
    {
        SwipeInput.OnSwipe -= OnSwipe;
        SwipeInput.OnTap -= OnTap;
    }

    void OnSwipe(SwipeInput.SwipeDirection dir)
    {
        switch (dir)
        {
            case SwipeInput.SwipeDirection.Up:
                if (isGrounded)
                {
                    isGrounded = false;
                    PlayAnimation(ANIM_JUMP, false);
                }
                break;
            case SwipeInput.SwipeDirection.Down:
                if (isGrounded && !isSliding)
                {
                    isSliding = true;
                    PlayAnimation(ANIM_SLIDE, false);
                    Invoke(nameof(EndSlide), 0.6f);
                }
                break;
        }
    }

    void OnTap()
    {
        PlayAnimation(ANIM_MAGIC, false);
    }

    void EndSlide()
    {
        isSliding = false;
        PlayAnimation(ANIM_RUN, true);
    }

    public void OnLanded()
    {
        isGrounded = true;
        if (!isSliding)
            PlayAnimation(ANIM_RUN, true);
    }

    void PlayAnimation(string animName, bool loop)
    {
        if (currentAnimation == animName) return;
        currentAnimation = animName;

        // When Spine-Unity runtime is imported, use:
        // skeletonAnimation.AnimationState.SetAnimation(0, animName, loop);

        // Fallback: trigger Animator parameter
        if (animator != null)
        {
            animator.Play(animName);
        }
    }
}
