using UnityEngine;
using UnityEngine.SceneManagement;
using System;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    public static event Action<int> OnScoreChanged;
    public static event Action<int> OnCrownShardCollected;
    public static event Action OnGameOver;
    public static event Action OnGameStart;

    [Header("Game Settings")]
    [SerializeField] private float startSpeed = 6f;
    [SerializeField] private float maxSpeed = 15f;
    [SerializeField] private float speedIncreaseRate = 0.1f;
    [SerializeField] private int totalCrownShards = 5;

    public float CurrentSpeed { get; private set; }
    public int Score { get; private set; }
    public int CrownShardsCollected { get; private set; }
    public bool IsPlaying { get; private set; }
    public float DistanceTraveled { get; private set; }

    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
    }

    void Start()
    {
        StartGame();
    }

    void Update()
    {
        if (!IsPlaying) return;

        // Increase speed over time
        CurrentSpeed = Mathf.Min(CurrentSpeed + speedIncreaseRate * Time.deltaTime, maxSpeed);

        // Track distance
        DistanceTraveled += CurrentSpeed * Time.deltaTime;

        // Score increases with distance
        int distanceScore = Mathf.FloorToInt(DistanceTraveled);
        if (distanceScore > Score)
        {
            Score = distanceScore;
            OnScoreChanged?.Invoke(Score);
        }
    }

    public void StartGame()
    {
        IsPlaying = true;
        CurrentSpeed = startSpeed;
        Score = 0;
        CrownShardsCollected = 0;
        DistanceTraveled = 0f;
        OnGameStart?.Invoke();
    }

    public void GameOver()
    {
        IsPlaying = false;
        OnGameOver?.Invoke();
    }

    public void AddScore(int points)
    {
        Score += points;
        OnScoreChanged?.Invoke(Score);
    }

    public void CollectCrownShard()
    {
        CrownShardsCollected++;
        OnCrownShardCollected?.Invoke(CrownShardsCollected);
        AddScore(100);
    }

    public void RestartGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

    public void LoadMainMenu()
    {
        SceneManager.LoadScene("MainMenu");
    }
}
