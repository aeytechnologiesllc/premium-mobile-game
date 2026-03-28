using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class UIManager : MonoBehaviour
{
    [Header("HUD")]
    [SerializeField] private TextMeshProUGUI scoreText;
    [SerializeField] private TextMeshProUGUI crownShardText;

    [Header("Game Over")]
    [SerializeField] private GameObject gameOverPanel;
    [SerializeField] private TextMeshProUGUI finalScoreText;
    [SerializeField] private Button restartButton;
    [SerializeField] private Button menuButton;

    [Header("Main Menu")]
    [SerializeField] private GameObject mainMenuPanel;
    [SerializeField] private Button playButton;

    void OnEnable()
    {
        GameManager.OnScoreChanged += UpdateScore;
        GameManager.OnCrownShardCollected += UpdateCrownShards;
        GameManager.OnGameOver += ShowGameOver;
        GameManager.OnGameStart += HideGameOver;
    }

    void OnDisable()
    {
        GameManager.OnScoreChanged -= UpdateScore;
        GameManager.OnCrownShardCollected -= UpdateCrownShards;
        GameManager.OnGameOver -= ShowGameOver;
        GameManager.OnGameStart -= HideGameOver;
    }

    void Start()
    {
        if (gameOverPanel != null) gameOverPanel.SetActive(false);

        if (restartButton != null)
            restartButton.onClick.AddListener(() => GameManager.Instance?.RestartGame());
        if (menuButton != null)
            menuButton.onClick.AddListener(() => GameManager.Instance?.LoadMainMenu());
        if (playButton != null)
            playButton.onClick.AddListener(() => GameManager.Instance?.StartGame());

        UpdateScore(0);
        UpdateCrownShards(0);
    }

    void UpdateScore(int score)
    {
        if (scoreText != null)
            scoreText.text = score.ToString("N0");
    }

    void UpdateCrownShards(int count)
    {
        if (crownShardText != null)
            crownShardText.text = $"{count} / 5";
    }

    void ShowGameOver()
    {
        if (gameOverPanel != null)
        {
            gameOverPanel.SetActive(true);
            if (finalScoreText != null)
                finalScoreText.text = $"Score: {GameManager.Instance?.Score ?? 0}";
        }
    }

    void HideGameOver()
    {
        if (gameOverPanel != null)
            gameOverPanel.SetActive(false);
    }
}
