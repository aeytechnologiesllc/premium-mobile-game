using UnityEngine;
using UnityEditor;
using UnityEditor.SceneManagement;

[InitializeOnLoad]
public class GameSetup
{
    static GameSetup()
    {
        EditorApplication.delayCall += SetupOnFirstRun;
    }

    static void SetupOnFirstRun()
    {
        // Check if setup already done
        if (EditorPrefs.GetBool("AeloraSetupDone", false)) return;

        Debug.Log("=== Aelora Game Auto-Setup ===");
        Debug.Log("Setting up game scene...");

        // Open the game scene
        string scenePath = "Assets/Scenes/GameScene.unity";
        if (System.IO.File.Exists(System.IO.Path.Combine(Application.dataPath, "../" + scenePath).Replace("/", System.IO.Path.DirectorySeparatorChar.ToString())))
        {
            // Scene exists, we can set it up
            Debug.Log("GameScene found. Open it from Assets/Scenes/GameScene.unity");
        }

        // Add required tags if they don't exist
        AddTag("Obstacle");
        AddTag("Collectible");
        AddTag("CrownShard");

        EditorPrefs.SetBool("AeloraSetupDone", true);
        Debug.Log("=== Aelora Setup Complete! ===");
        Debug.Log("Open Assets/Scenes/GameScene.unity and press Play to run the game.");
        Debug.Log("Use Arrow Keys or WASD to control: Up=Jump, Down=Slide, Left/Right=Dodge, Space=Magic");
    }

    static void AddTag(string tag)
    {
        SerializedObject tagManager = new SerializedObject(
            AssetDatabase.LoadAllAssetsAtPath("ProjectSettings/TagManager.asset")[0]);
        SerializedProperty tagsProp = tagManager.FindProperty("tags");

        // Check if tag already exists
        for (int i = 0; i < tagsProp.arraySize; i++)
        {
            if (tagsProp.GetArrayElementAtIndex(i).stringValue == tag)
                return;
        }

        tagsProp.InsertArrayElementAtIndex(tagsProp.arraySize);
        tagsProp.GetArrayElementAtIndex(tagsProp.arraySize - 1).stringValue = tag;
        tagManager.ApplyModifiedProperties();
        Debug.Log($"Added tag: {tag}");
    }
}
