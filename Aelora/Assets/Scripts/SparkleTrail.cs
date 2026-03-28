using UnityEngine;

public class SparkleTrail : MonoBehaviour
{
    [SerializeField] private ParticleSystem sparkleParticles;
    [SerializeField] private ParticleSystem slideParticles;

    private PlayerController player;

    void Start()
    {
        player = GetComponentInParent<PlayerController>();
    }

    public void SetSliding(bool sliding)
    {
        if (slideParticles == null) return;

        if (sliding && !slideParticles.isPlaying)
            slideParticles.Play();
        else if (!sliding && slideParticles.isPlaying)
            slideParticles.Stop();
    }
}
