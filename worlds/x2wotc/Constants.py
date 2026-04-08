GAME_NAME: str = "XCOM 2 War of the Chosen"
CLIENT_NAME: str = f"{GAME_NAME} Client"

GOAL_VALUE_TO_EVENT: dict[int, str] = {
    0: "Victory",
    1: "Broadcast",
    2: "Stronghold1",
    3: "Stronghold2",
    4: "Stronghold3"
}
GOAL_EVENT_TO_VALUE: dict[str, int] = {event: value for value, event in GOAL_VALUE_TO_EVENT.items()}
