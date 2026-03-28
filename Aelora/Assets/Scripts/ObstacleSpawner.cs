using UnityEngine;

public class ObstacleSpawner : MonoBehaviour
{
    [Header("Spawning")]
    [SerializeField] private GameObject[] obstaclePrefabs;
    [SerializeField] private GameObject[] collectiblePrefabs;
    [SerializeField] private GameObject crownShardPrefab;
    [SerializeField] private float spawnDistance = 15f;
    [SerializeField] private float minSpawnInterval = 0.8f;
    [SerializeField] private float maxSpawnInterval = 2.5f;
    [SerializeField] private float collectibleChance = 0.4f;

    [Header("Lanes")]
    [SerializeField] private float laneWidth = 2.5f;

    private float spawnTimer;
    private float nextSpawnTime;
    private int crownShardsSpawned;

    void Start()
    {
        SetNextSpawnTime();
    }

    void Update()
    {
        if (GameManager.Instance == null || !GameManager.Instance.IsPlaying) return;

        spawnTimer += Time.deltaTime;
        if (spawnTimer >= nextSpawnTime)
        {
            SpawnObstacle();
            spawnTimer = 0f;
            SetNextSpawnTime();
        }
    }

    void SetNextSpawnTime()
    {
        // Spawn faster as speed increases
        float speedFactor = GameManager.Instance != null
            ? Mathf.InverseLerp(6f, 15f, GameManager.Instance.CurrentSpeed)
            : 0f;
        float interval = Mathf.Lerp(maxSpawnInterval, minSpawnInterval, speedFactor);
        nextSpawnTime = interval + Random.Range(-0.2f, 0.2f);
    }

    void SpawnObstacle()
    {
        int lane = Random.Range(0, 3);
        float xPos = (lane - 1) * laneWidth;
        Vector3 spawnPos = new Vector3(xPos, 0f, 0f) + Vector3.right * spawnDistance;

        // Decide what to spawn
        if (Random.value < collectibleChance)
        {
            SpawnCollectible(spawnPos, lane);
        }
        else
        {
            SpawnHazard(spawnPos);
        }

        // Occasionally spawn crown shards
        if (crownShardsSpawned < 5 && Random.value < 0.02f && crownShardPrefab != null)
        {
            Vector3 shardPos = new Vector3((Random.Range(0, 3) - 1) * laneWidth, 1.5f, 0f)
                + Vector3.right * spawnDistance;
            GameObject shard = Instantiate(crownShardPrefab, shardPos, Quaternion.identity);
            shard.AddComponent<ObstacleMovement>();
            crownShardsSpawned++;
        }
    }

    void SpawnHazard(Vector3 pos)
    {
        if (obstaclePrefabs.Length == 0) return;

        int index = Random.Range(0, obstaclePrefabs.Length);
        GameObject obstacle = Instantiate(obstaclePrefabs[index], pos, Quaternion.identity);
        obstacle.AddComponent<ObstacleMovement>();
    }

    void SpawnCollectible(Vector3 pos, int lane)
    {
        if (collectiblePrefabs.Length == 0) return;

        // Spawn a line of collectibles
        int count = Random.Range(3, 7);
        float spacing = 1.2f;
        float yOffset = Random.value > 0.5f ? 1.5f : 0.5f;

        for (int i = 0; i < count; i++)
        {
            Vector3 collectPos = pos + Vector3.right * (i * spacing) + Vector3.up * yOffset;
            int prefabIndex = Random.Range(0, collectiblePrefabs.Length);
            GameObject collectible = Instantiate(collectiblePrefabs[prefabIndex], collectPos, Quaternion.identity);
            collectible.AddComponent<ObstacleMovement>();
        }
    }
}
