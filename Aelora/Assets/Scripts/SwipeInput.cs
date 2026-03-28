using UnityEngine;
using System;

public class SwipeInput : MonoBehaviour
{
    public static event Action<SwipeDirection> OnSwipe;
    public static event Action OnTap;

    [SerializeField] private float minSwipeDistance = 50f;
    [SerializeField] private float maxSwipeTime = 0.5f;

    private Vector2 touchStartPos;
    private float touchStartTime;
    private bool isSwiping;

    public enum SwipeDirection
    {
        Up,
        Down,
        Left,
        Right
    }

    void Update()
    {
        HandleTouchInput();
        HandleKeyboardInput();
    }

    void HandleTouchInput()
    {
        if (Input.touchCount == 0) return;

        Touch touch = Input.GetTouch(0);

        switch (touch.phase)
        {
            case TouchPhase.Began:
                touchStartPos = touch.position;
                touchStartTime = Time.time;
                isSwiping = true;
                break;

            case TouchPhase.Ended:
                if (!isSwiping) break;
                isSwiping = false;

                float swipeTime = Time.time - touchStartTime;
                Vector2 swipeDelta = touch.position - touchStartPos;
                float swipeDistance = swipeDelta.magnitude;

                if (swipeTime > maxSwipeTime)
                {
                    // Too slow, treat as tap
                    OnTap?.Invoke();
                    return;
                }

                if (swipeDistance < minSwipeDistance)
                {
                    // Too short, treat as tap
                    OnTap?.Invoke();
                    return;
                }

                // Determine swipe direction
                if (Mathf.Abs(swipeDelta.x) > Mathf.Abs(swipeDelta.y))
                {
                    OnSwipe?.Invoke(swipeDelta.x > 0 ? SwipeDirection.Right : SwipeDirection.Left);
                }
                else
                {
                    OnSwipe?.Invoke(swipeDelta.y > 0 ? SwipeDirection.Up : SwipeDirection.Down);
                }
                break;

            case TouchPhase.Canceled:
                isSwiping = false;
                break;
        }
    }

    void HandleKeyboardInput()
    {
        // Keyboard fallback for testing in editor
        if (Input.GetKeyDown(KeyCode.UpArrow) || Input.GetKeyDown(KeyCode.W))
            OnSwipe?.Invoke(SwipeDirection.Up);
        if (Input.GetKeyDown(KeyCode.DownArrow) || Input.GetKeyDown(KeyCode.S))
            OnSwipe?.Invoke(SwipeDirection.Down);
        if (Input.GetKeyDown(KeyCode.LeftArrow) || Input.GetKeyDown(KeyCode.A))
            OnSwipe?.Invoke(SwipeDirection.Left);
        if (Input.GetKeyDown(KeyCode.RightArrow) || Input.GetKeyDown(KeyCode.D))
            OnSwipe?.Invoke(SwipeDirection.Right);
        if (Input.GetKeyDown(KeyCode.Space))
            OnTap?.Invoke();
    }
}
