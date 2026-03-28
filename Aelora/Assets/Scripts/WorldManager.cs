using UnityEngine;

/// <summary>
/// Manages world/biome transitions as the player progresses.
/// Each world has its own background layers and obstacle themes.
/// </summary>
public class WorldManager : MonoBehaviour
{
    [System.Serializable]
    public class WorldData
    {
        public string worldName;
        public Sprite[] backgroundLayers; // far, mid, near
        public float[] parallaxSpeeds;
        public Color ambientColor;
        public GameObject[] obstaclePrefabs;
        public GameObject[] collectiblePrefabs;
        public AudioClip music;
    }

    [SerializeField] private WorldData[] worlds;
    [SerializeField] private SpriteRenderer[] backgroundRenderers;
    [SerializeField] private float worldTransitionDistance = 500f;

    private int currentWorldIndex;

    void Start()
    {
        if (worlds != null && worlds.Length > 0)
            LoadWorld(0);
    }

    void Update()
    {
        if (GameManager.Instance == null || !GameManager.Instance.IsPlaying) return;

        // Check for world transition
        int expectedWorld = Mathf.FloorToInt(GameManager.Instance.DistanceTraveled / worldTransitionDistance);
        expectedWorld = Mathf.Clamp(expectedWorld, 0, worlds.Length - 1);

        if (expectedWorld != currentWorldIndex)
        {
            TransitionToWorld(expectedWorld);
        }
    }

    void LoadWorld(int index)
    {
        if (index < 0 || index >= worlds.Length) return;

        currentWorldIndex = index;
        WorldData world = worlds[index];

        // Set backgrounds
        if (backgroundRenderers != null && world.backgroundLayers != null)
        {
            for (int i = 0; i < backgroundRenderers.Length && i < world.backgroundLayers.Length; i++)
            {
                backgroundRenderers[i].sprite = world.backgroundLayers[i];

                var parallax = backgroundRenderers[i].GetComponent<ParallaxBackground>();
                if (parallax != null && world.parallaxSpeeds != null && i < world.parallaxSpeeds.Length)
                {
                    // Parallax speed is set via serialized field, so we'd need a setter
                }
            }
        }
    }

    void TransitionToWorld(int newIndex)
    {
        // Smooth transition between worlds
        LoadWorld(newIndex);
    }

    public WorldData GetCurrentWorld()
    {
        if (worlds == null || currentWorldIndex >= worlds.Length) return null;
        return worlds[currentWorldIndex];
    }

    public string GetCurrentWorldName()
    {
        var world = GetCurrentWorld();
        return world?.worldName ?? "Unknown";
    }
}
