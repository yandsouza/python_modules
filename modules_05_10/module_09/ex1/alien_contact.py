from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def custom_validation(self) -> "AlienContact":

        if self.contact_id.startswith("AC") is False:
            raise ValueError("Contact ID must start with "
                             "'AC' (Alien Contact)")

        if self.contact_type == ContactType.PHYSICAL and \
                self.is_verified is False:
            raise ValueError("Physical contact reports "
                             "must be verifed")

        if self.contact_type == ContactType.TELEPATHIC and \
                self.witness_count < 3:
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        if self.signal_strength > 7 and \
                self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should "
                             "include received messages")

        return self


def main() -> None:
    print("Alien Contact Log Validation\n"
          "========================================")
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True)

    print("Valid contact created:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")
    print()

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True)
    except ValidationError as error:
        print("========================================")
        print("Expected validation error:")
        print(error.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
