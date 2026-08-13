from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":

        if self.mission_id.startswith("M") is False:
            raise ValueError("Mission ID must start with 'M'")

        if not any(crew.rank in [Rank.CAPTAIN, Rank.COMMANDER]
                   for crew in self.crew):
            raise ValueError("Mission must have "
                             "at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = sum(m.years_experience >= 5 for m in self.crew)
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")

        if all(crew.is_active for crew in self.crew) is False:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation\n"
          "========================================")
    commander = CrewMember(
        member_id="TI42", name="Sarah Connor", rank=Rank.COMMANDER,
        age=52, specialization="Mission Command", years_experience=35)

    lieutenant = CrewMember(
        member_id="MV32", name="John Smith", rank=Rank.LIEUTENANT,
        age=25, specialization="Navigation", years_experience=8)

    officer = CrewMember(
        member_id="YK10", name="Alice Johnson", rank=Rank.OFFICER,
        age=21, specialization="Engineering", years_experience=2)
    crew = [commander, lieutenant, officer]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 2, 12, 15, 0),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0)

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) "
              f"- {member.specialization}")
    print()

    try:
        crew = [lieutenant, officer]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 2, 12, 15, 0),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0)
    except ValidationError as error:
        print("========================================")
        print("Expected validation error:")
        print(error.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
