# APIs - App States

This page shows all possible app states and
their transitions.

This information is only relevant if you plan on using the API feature.

## Top States
```mermaid

flowchart TD
    IDLE --> CONNECTING
    CONNECTING --> |Down state change| CONNECTING
    CONNECTING --> IDLE
    CONNECTING --> CONNECTED
    CONNECTED --> |Down state change| CONNECTED
    CONNECTED --> IDLE
    CONNECTED --> RECONNECTING
    RECONNECTING --> |Retry| RECONNECTING
    RECONNECTING --> CONNECTED
    RECONNECTING --> IDLE


    classDef transition fill:#050,color:#ddd;
```


## Top State: IDLE
```mermaid

flowchart TD
    Start --> IDLE
    IDLE --> CONNECTING
    CONNECTING:::transition --> End


    classDef transition fill:#050,color:#ddd;
```


## Top State: CONNECTING
```mermaid

flowchart TD
    Start --> SEARCHING
    Start --> CONNECTING
    SEARCHING --> CONNECTING
    SEARCHING --> IDLE
    CONNECTING --> PRE_PASSWORD
    CONNECTING --> SYNCHRONIZING
    CONNECTING --> CONNECTION_LOST
    CONNECTING --> IDLE
    PRE_PASSWORD --> SYNCHRONIZING
    PRE_PASSWORD --> CONNECTION_LOST
    PRE_PASSWORD --> IDLE
    SYNCHRONIZING --> CONNECTED
    SYNCHRONIZING --> POST_PASSWORD
    SYNCHRONIZING --> CONNECTION_LOST
    SYNCHRONIZING --> SYNC_ERROR
    SYNCHRONIZING --> IDLE
    SYNC_ERROR --> CONNECTING
    SYNC_ERROR --> IDLE
    POST_PASSWORD --> CONNECTED
    POST_PASSWORD --> CONNECTION_LOST
    POST_PASSWORD --> IDLE
    CONNECTION_LOST --> CONNECTING
    CONNECTION_LOST --> IDLE
    IDLE:::transition --> End
    CONNECTED:::transition --> End


    classDef transition fill:#050,color:#ddd;
```


## Top State: CONNECTED
```mermaid

flowchart TD
    Start --> CONNECTED
    CONNECTED --> BACKGROUND_SYNC
    CONNECTED --> SCENE_RECALL
    CONNECTED --> RECONNECTING
    CONNECTED --> CONNECTION_LOST
    CONNECTED --> IDLE
    CONNECTION_LOST --> RECONNECTING
    CONNECTION_LOST --> IDLE
    BACKGROUND_SYNC --> CONNECTED
    BACKGROUND_SYNC --> CONNECTION_LOST
    BACKGROUND_SYNC --> IDLE
    SCENE_RECALL --> CONNECTED
    SCENE_RECALL --> CONNECTION_LOST
    SCENE_RECALL --> IDLE
    RECONNECTING:::transition --> End
    IDLE:::transition --> End


    classDef transition fill:#050,color:#ddd;
```


## Top State: RECONNECTING
```mermaid

flowchart TD
    Start --> CONNECTING
    Start --> CONNECTION_LOST
    CONNECTING --> SYNCHRONIZING
    CONNECTING --> CONNECTION_LOST
    CONNECTING --> IDLE
    CONNECTION_LOST --> CONNECTING
    CONNECTION_LOST --> IDLE
    SYNCHRONIZING --> CONNECTED
    SYNCHRONIZING --> CONNECTION_LOST
    SYNCHRONIZING --> SYNC_ERROR
    SYNCHRONIZING --> IDLE
    SYNC_ERROR --> CONNECTING
    SYNC_ERROR --> IDLE
    IDLE:::transition --> End
    CONNECTED:::transition --> End


    classDef transition fill:#050,color:#ddd;
```
