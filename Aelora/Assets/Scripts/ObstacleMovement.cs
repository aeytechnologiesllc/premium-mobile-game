using UnityEngine;

public class ObstacleMovement : MonoBehaviour
{
    [SerializeField] private float destroyDistance = -15f;

    void Update()
    {
        if (GameManager.Instance == null || !GameManager.Instance.IsPlaying) return;

        float speed = GameManager.Instance.CurrentSpeed;
        transform.Translate(Vector3.left * speed * Time.deltaTime);

        if (transform.position.x < destroyDistance)
        {
            Destroy(gameObject);
        }
    }
}
