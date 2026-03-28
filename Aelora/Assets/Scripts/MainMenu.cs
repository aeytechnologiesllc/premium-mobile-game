using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using TMPro;

public class MainMenu : MonoBehaviour
{
    [SerializeField] private Button playButton;
    [SerializeField] private Button outfitsButton;
    [SerializeField] private Button settingsButton;
    [SerializeField] private GameObject outfitPanel;
    [SerializeField] private GameObject settingsPanel;
    [SerializeField] private TextMeshProUGUI titleText;

    [Header("Parallax Title Screen")]
    [SerializeField] private Transform[] backgroundLayers;
    [SerializeField] private float[] layerSpeeds;

    void Start()
    {
        if (playButton != null)
            playButton.onClick.AddListener(PlayGame);
        if (outfitsButton != null)
            outfitsButton.onClick.AddListener(ToggleOutfits);
        if (settingsButton != null)
            settingsButton.onClick.AddListener(ToggleSettings);

        if (outfitPanel != null) outfitPanel.SetActive(false);
        if (settingsPanel != null) settingsPanel.SetActive(false);
    }

    void Update()
    {
        // Gentle parallax movement on title screen
        if (backgroundLayers == null) return;

        for (int i = 0; i < backgroundLayers.Length; i++)
        {
            if (backgroundLayers[i] == null || i >= layerSpeeds.Length) continue;

            float offset = Mathf.Sin(Time.time * layerSpeeds[i] * 0.3f) * 0.5f;
            Vector3 pos = backgroundLayers[i].localPosition;
            pos.x = offset;
            backgroundLayers[i].localPosition = pos;
        }
    }

    void PlayGame()
    {
        SceneManager.LoadScene("GameScene");
    }

    void ToggleOutfits()
    {
        if (outfitPanel != null)
            outfitPanel.SetActive(!outfitPanel.activeSelf);
        if (settingsPanel != null)
            settingsPanel.SetActive(false);
    }

    void ToggleSettings()
    {
        if (settingsPanel != null)
            settingsPanel.SetActive(!settingsPanel.activeSelf);
        if (outfitPanel != null)
            outfitPanel.SetActive(false);
    }
}
