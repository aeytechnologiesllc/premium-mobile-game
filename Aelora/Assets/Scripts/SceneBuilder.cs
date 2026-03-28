using UnityEngine;

/// <summary>
/// Attach to an empty GameObject in any scene.
/// On Awake, it builds all game objects needed if they don't exist.
/// This ensures the game works even with a minimal scene file.
/// </summary>
public class SceneBuilder : MonoBehaviour
{
    void Awake()
    {
        // Only build if GameManager doesn't exist
        if (FindAnyObjectByType<GameManager>() != null) return;

        Debug.Log("SceneBuilder: Setting up game objects...");

        // Create GameManager
        var gmObj = new GameObject("GameManager");
        gmObj.AddComponent<GameManager>();

        // Create InputManager
        var inputObj = new GameObject("InputManager");
        inputObj.AddComponent<SwipeInput>();

        // Create Player
        var playerObj = new GameObject("Player");
        playerObj.tag = "Player";
        playerObj.transform.position = new Vector3(-3, -2.5f, 0);
        var sr = playerObj.AddComponent<SpriteRenderer>();
        sr.color = new Color(0.2f, 0.35f, 0.7f, 1f); // Blue placeholder
        sr.sortingOrder = 10;
        var collider = playerObj.AddComponent<BoxCollider2D>();
        collider.isTrigger = true;
        collider.size = new Vector2(0.8f, 1.5f);
        collider.offset = new Vector2(0, 0.75f);
        playerObj.AddComponent<PlayerController>();
        playerObj.AddComponent<SpinePlayerController>();

        // Create Ground visual
        var groundObj = new GameObject("Ground");
        groundObj.transform.position = new Vector3(0, -3.5f, 0);
        groundObj.transform.localScale = new Vector3(30, 0.5f, 1);
        var groundSr = groundObj.AddComponent<SpriteRenderer>();
        groundSr.color = new Color(0.15f, 0.1f, 0.05f, 1f);

        // Create Background layers
        CreateBackground("Background_Far", new Vector3(0, 0, 5), 3f, -10, 0.2f);
        CreateBackground("Background_Mid", new Vector3(0, 0, 3), 2.5f, -5, 0.5f);

        // Create ObstacleSpawner
        var spawnerObj = new GameObject("ObstacleSpawner");
        spawnerObj.AddComponent<ObstacleSpawner>();

        // Create Camera setup
        var cam = Camera.main;
        if (cam != null)
        {
            cam.backgroundColor = new Color(0.05f, 0.03f, 0.1f, 1f);
            cam.orthographicSize = 5;
            cam.transform.position = new Vector3(0, 1, -10);
            var follow = cam.gameObject.AddComponent<CameraFollow>();
        }

        Debug.Log("SceneBuilder: Game ready! Use Arrow Keys: Up=Jump, Down=Slide, Left/Right=Dodge, Space=Magic");
    }

    void CreateBackground(string name, Vector3 pos, float scale, int sortOrder, float parallaxFactor)
    {
        var obj = new GameObject(name);
        obj.transform.position = pos;
        obj.transform.localScale = new Vector3(scale, scale, 1);
        var sr = obj.AddComponent<SpriteRenderer>();
        sr.sortingOrder = sortOrder;

        // Try to load background sprite
        var sprite = Resources.Load<Sprite>("Backgrounds/moonlit_garden_bg");
        if (sprite != null) sr.sprite = sprite;

        var parallax = obj.AddComponent<ParallaxBackground>();
    }
}
