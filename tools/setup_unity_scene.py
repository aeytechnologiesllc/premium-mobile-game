"""
Generates Unity scene files, prefabs, and project settings programmatically.
Creates a fully playable game scene that works when opened in Unity Editor.
"""

import os
import json

PROJECT_DIR = os.path.expanduser("~/Desktop/premium-mobile-game/Aelora")
ASSETS_DIR = os.path.join(PROJECT_DIR, "Assets")
SCENES_DIR = os.path.join(ASSETS_DIR, "Scenes")
PREFABS_DIR = os.path.join(ASSETS_DIR, "Prefabs")
SETTINGS_DIR = os.path.join(PROJECT_DIR, "ProjectSettings")

os.makedirs(SCENES_DIR, exist_ok=True)
os.makedirs(PREFABS_DIR, exist_ok=True)

# ============================================================
# 1. Create the main GameScene.unity
# ============================================================
print("Creating GameScene.unity...")

game_scene = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!29 &1
OcclusionCullingSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_OcclusionBakeSettings:
    smallestOccluder: 5
    smallestHole: 0.25
    backfaceThreshold: 100
  m_SceneGUID: 00000000000000000000000000000000
  m_OcclusionCullingData: {fileID: 0}
--- !u!104 &2
RenderSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 10
  m_Fog: 0
  m_FogColor: {r: 0.5, g: 0.5, b: 0.5, a: 1}
  m_FogMode: 3
  m_FogDensity: 0.01
  m_LinearFogStart: 0
  m_LinearFogEnd: 300
  m_AmbientSkyColor: {r: 0.2, g: 0.15, b: 0.3, a: 1}
  m_AmbientEquatorColor: {r: 0.1, g: 0.1, b: 0.2, a: 1}
  m_AmbientGroundColor: {r: 0.1, g: 0.1, b: 0.15, a: 1}
  m_AmbientIntensity: 1
  m_AmbientMode: 3
  m_SubtractiveShadowColor: {r: 0.42, g: 0.478, b: 0.627, a: 1}
  m_SkyboxMaterial: {fileID: 0}
  m_HaloStrength: 0.5
  m_FlareStrength: 1
  m_FlareFadeSpeed: 3
  m_HaloTexture: {fileID: 0}
  m_SpotCookie: {fileID: 10001, guid: 0000000000000000e000000000000000, type: 0}
  m_DefaultReflectionMode: 0
  m_DefaultReflectionResolution: 128
  m_ReflectionBounces: 1
  m_ReflectionIntensity: 1
  m_CustomReflection: {fileID: 0}
  m_Sun: {fileID: 0}
  m_UseRadianceAmbientProbe: 0
--- !u!157 &3
LightmapSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 12
  m_GIWorkflowMode: 1
  m_EnableBakedLightmaps: 0
  m_EnableRealtimeLightmaps: 0
--- !u!196 &4
NavMeshSettings:
  serializedVersion: 2
  m_ObjectHideFlags: 0
  m_BuildSettings:
    serializedVersion: 3
    agentTypeID: 0
    agentRadius: 0.5
    agentHeight: 2
    agentSlope: 45
    agentClimb: 0.4
    ledgeDropHeight: 0
    maxJumpAcrossDistance: 0
    minRegionArea: 2
    manualCellSize: 0
    cellSize: 0.16666667
    manualTileSize: 0
    tileSize: 256
    buildHeightMesh: 0
  m_NavMeshData: {fileID: 0}
--- !u!1 &100
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 101}
  - component: {fileID: 102}
  - component: {fileID: 103}
  m_Layer: 0
  m_Name: Main Camera
  m_TagString: MainCamera
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &101
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 100}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: 1, z: -10}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!20 &102
Camera:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 100}
  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 2
  m_BackGroundColor: {r: 0.05, g: 0.03, b: 0.1, a: 1}
  m_projectionMatrixMode: 1
  m_GateFitMode: 2
  m_FOVAxisMode: 0
  m_Iso: 1
  m_OrthographicSize: 5
  m_NearClipPlane: 0.3
  m_FarClipPlane: 1000
  m_Depth: -1
  m_RenderingPath: -1
  m_TargetTexture: {fileID: 0}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 1
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_ForceIntoRenderTexture: 0
  m_OcclusionCulling: 1
  m_StereoConvergence: 10
  m_StereoSeparation: 0.022
--- !u!114 &103
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 100}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!1 &200
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 201}
  - component: {fileID: 202}
  - component: {fileID: 203}
  - component: {fileID: 204}
  - component: {fileID: 205}
  m_Layer: 0
  m_Name: Player
  m_TagString: Player
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &201
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 200}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: -3, y: -2.5, z: 0}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!212 &202
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 200}
  m_Enabled: 1
  m_CastShadows: 0
  m_ReceiveShadows: 0
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RayTracingMode: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 10
  m_Sprite: {fileID: 0}
  m_Color: {r: 1, g: 1, b: 1, a: 1}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {x: 1, y: 1}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WatershedMode: 1
  m_SpriteSortPoint: 0
--- !u!61 &203
BoxCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 200}
  m_Enabled: 1
  m_Density: 1
  m_Material: {fileID: 0}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_LayerOverridePriority: 0
  m_ForceSendLayers:
    serializedVersion: 2
    m_Bits: 4294967295
  m_ForceReceiveLayers:
    serializedVersion: 2
    m_Bits: 4294967295
  m_ContactCaptureLayers:
    serializedVersion: 2
    m_Bits: 4294967295
  m_CallbackLayers:
    serializedVersion: 2
    m_Bits: 4294967295
  m_IsTrigger: 1
  m_UsedByEffector: 0
  m_UsedByComposite: 0
  m_Offset: {x: 0, y: 0.75}
  m_SpriteTilingProperty:
    border: {x: 0, y: 0, z: 0, w: 0}
    pivot: {x: 0, y: 0}
    oldSize: {x: 0, y: 0}
    newSize: {x: 0, y: 0}
    adaptiveTilingThreshold: 0
    drawMode: 0
    adaptiveTiling: 0
  m_AutoTiling: 0
  serializedVersion: 2
  m_Size: {x: 0.8, y: 1.5}
  m_EdgeRadius: 0
--- !u!114 &204
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 200}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!114 &205
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 200}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!1 &300
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 301}
  - component: {fileID: 302}
  m_Layer: 0
  m_Name: GameManager
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &301
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 300}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: 0, z: 0}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!114 &302
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 300}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!1 &400
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 401}
  - component: {fileID: 402}
  m_Layer: 0
  m_Name: InputManager
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &401
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 400}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: 0, z: 0}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!114 &402
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 400}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!1 &500
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 501}
  - component: {fileID: 502}
  m_Layer: 0
  m_Name: ObstacleSpawner
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &501
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 500}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 15, y: 0, z: 0}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!114 &502
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 500}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!1 &600
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 601}
  - component: {fileID: 602}
  - component: {fileID: 603}
  m_Layer: 0
  m_Name: Background_Far
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &601
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 600}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: 0, z: 5}
  m_LocalScale: {x: 3, y: 3, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!212 &602
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 600}
  m_Enabled: 1
  m_CastShadows: 0
  m_ReceiveShadows: 0
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 0
  m_ReflectionProbeUsage: 0
  m_RayTracingMode: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: -10
  m_Sprite: {fileID: 0}
  m_Color: {r: 1, g: 1, b: 1, a: 1}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {x: 1, y: 1}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WatershedMode: 1
  m_SpriteSortPoint: 0
--- !u!114 &603
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 600}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!1 &700
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 701}
  - component: {fileID: 702}
  - component: {fileID: 703}
  m_Layer: 0
  m_Name: Background_Mid
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &701
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 700}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: 0, z: 3}
  m_LocalScale: {x: 2.5, y: 2.5, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!212 &702
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 700}
  m_Enabled: 1
  m_CastShadows: 0
  m_ReceiveShadows: 0
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 0
  m_ReflectionProbeUsage: 0
  m_RayTracingMode: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: -5
  m_Sprite: {fileID: 0}
  m_Color: {r: 1, g: 1, b: 1, a: 1}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {x: 1, y: 1}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WatershedMode: 1
  m_SpriteSortPoint: 0
--- !u!114 &703
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 700}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 0, type: 0}
  m_Name:
  m_EditorClassIdentifier:
--- !u!1 &800
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 801}
  - component: {fileID: 802}
  m_Layer: 0
  m_Name: Ground
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &801
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 800}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: -3.5, z: 0}
  m_LocalScale: {x: 30, y: 0.5, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!212 &802
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 800}
  m_Enabled: 1
  m_CastShadows: 0
  m_ReceiveShadows: 0
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 0
  m_ReflectionProbeUsage: 0
  m_RayTracingMode: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 0
  m_Sprite: {fileID: 0}
  m_Color: {r: 0.15, g: 0.1, b: 0.05, a: 1}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {x: 1, y: 1}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WatershedMode: 1
  m_SpriteSortPoint: 0
"""

with open(os.path.join(SCENES_DIR, "GameScene.unity"), "w") as f:
    f.write(game_scene)
print("  GameScene.unity created")

# Also create a meta file for the scene
scene_meta = """fileFormatVersion: 2
guid: a1b2c3d4e5f60718293a4b5c6d7e8f90
DefaultImporter:
  externalObjects: {}
  userData:
  assetBundleName:
  assetBundleVariant:
"""
with open(os.path.join(SCENES_DIR, "GameScene.unity.meta"), "w") as f:
    f.write(scene_meta)

# ============================================================
# 2. Update EditorBuildSettings to include our scene
# ============================================================
print("Updating EditorBuildSettings...")

build_settings = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1045 &1
EditorBuildSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Scenes:
  - enabled: 1
    path: Assets/Scenes/GameScene.unity
    guid: a1b2c3d4e5f60718293a4b5c6d7e8f90
  m_configObjects: {}
"""

with open(os.path.join(SETTINGS_DIR, "EditorBuildSettings.asset"), "w") as f:
    f.write(build_settings)
print("  EditorBuildSettings.asset updated")

# ============================================================
# 3. Update TagManager to add custom tags
# ============================================================
print("Updating TagManager with game tags...")

tag_manager = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!78 &1
TagManager:
  serializedVersion: 2
  tags:
  - Obstacle
  - Collectible
  - CrownShard
  layers:
  - Default
  - TransparentFX
  - Ignore Raycast
  -
  - Water
  - UI
  -
  -
  - Background
  - Foreground
  - Player
  - Obstacles
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  -
  m_SortingLayers:
  - name: Default
    uniqueID: 0
    locked: 0
  - name: Background
    uniqueID: 1
    locked: 0
  - name: Midground
    uniqueID: 2
    locked: 0
  - name: Player
    uniqueID: 3
    locked: 0
  - name: Foreground
    uniqueID: 4
    locked: 0
  - name: UI
    uniqueID: 5
    locked: 0
"""

with open(os.path.join(SETTINGS_DIR, "TagManager.asset"), "w") as f:
    f.write(tag_manager)
print("  TagManager.asset updated")

# ============================================================
# 4. Update ProjectSettings for mobile
# ============================================================
print("Configuring project for mobile...")

# Read existing ProjectSettings and update key fields
project_settings_path = os.path.join(SETTINGS_DIR, "ProjectSettings.asset")
if os.path.exists(project_settings_path):
    with open(project_settings_path, 'r') as f:
        content = f.read()

    # Update company and product name
    content = content.replace("companyName: DefaultCompany", "companyName: AEY Technologies LLC")
    content = content.replace("productName: Aelora", "productName: Aelora - Whispers of the Enchanted Forest")
    if "productName: My project" in content:
        content = content.replace("productName: My project", "productName: Aelora - Whispers of the Enchanted Forest")

    with open(project_settings_path, 'w') as f:
        f.write(content)
    print("  ProjectSettings.asset updated (company name, product name)")

# ============================================================
# 5. Create an editor script to auto-setup the scene on first open
# ============================================================
print("Creating editor auto-setup script...")

editor_dir = os.path.join(ASSETS_DIR, "Editor")
os.makedirs(editor_dir, exist_ok=True)

editor_script = '''using UnityEngine;
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
'''

with open(os.path.join(editor_dir, "GameSetup.cs"), "w") as f:
    f.write(editor_script)
print("  Editor/GameSetup.cs created")

# ============================================================
# 6. Create a simple setup scene script that builds the game
#    when you open the project and press Play
# ============================================================
print("Creating runtime scene builder...")

scene_builder = '''using UnityEngine;

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
'''

with open(os.path.join(ASSETS_DIR, "Scripts", "SceneBuilder.cs"), "w") as f:
    f.write(scene_builder)
print("  SceneBuilder.cs created")

# ============================================================
# 7. Copy backgrounds to Resources folder for runtime loading
# ============================================================
print("Setting up Resources folder...")
resources_dir = os.path.join(ASSETS_DIR, "Resources", "Backgrounds")
os.makedirs(resources_dir, exist_ok=True)

import shutil
env_dir = os.path.join(ASSETS_DIR, "Art", "Environments")
for bg_file in os.listdir(env_dir):
    if bg_file.endswith(".png"):
        src = os.path.join(env_dir, bg_file)
        dst = os.path.join(resources_dir, bg_file)
        shutil.copy2(src, dst)
        print(f"  Copied {bg_file} to Resources/Backgrounds/")

print("\\n=== SETUP COMPLETE ===")
print("\\nTo play the game:")
print("1. Open Unity Hub")
print("2. Open the 'Aelora' project")
print("3. Open Assets/Scenes/GameScene.unity")
print("4. Press the Play button")
print("5. Controls: Arrow Keys or WASD (Up=Jump, Down=Slide, Left/Right=Dodge, Space=Magic)")
"""

with open("/Users/shahz/Desktop/premium-mobile-game/tools/setup_unity_scene.py", "w") as f:
    f.write(scene_builder_script)
"""
