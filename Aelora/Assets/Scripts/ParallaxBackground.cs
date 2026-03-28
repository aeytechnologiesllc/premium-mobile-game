using UnityEngine;

public class ParallaxBackground : MonoBehaviour
{
    [SerializeField] private float parallaxFactor = 0.5f;
    [SerializeField] private bool infiniteScrolling = true;

    private float spriteWidth;
    private Vector3 startPosition;
    private float totalMoved;

    void Start()
    {
        startPosition = transform.position;

        SpriteRenderer sr = GetComponent<SpriteRenderer>();
        if (sr != null)
        {
            spriteWidth = sr.bounds.size.x;
        }
    }

    void Update()
    {
        if (GameManager.Instance == null || !GameManager.Instance.IsPlaying) return;

        float speed = GameManager.Instance.CurrentSpeed * parallaxFactor;
        transform.Translate(Vector3.left * speed * Time.deltaTime);

        totalMoved += speed * Time.deltaTime;

        if (infiniteScrolling && totalMoved >= spriteWidth)
        {
            transform.position = startPosition;
            totalMoved = 0f;
        }
    }
}
