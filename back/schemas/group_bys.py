from pydantic import BaseModel, Field

class GroupByTypes(BaseModel):
    GROPING: int = 0
    STALKING: int = 0
    UNWANTED_PHOTOS: int = 0
    UNWANTED_COMMENTS: int = 0
    THREATENING: int = 0
    FLASHING: int = 0

class GroupByGenders(BaseModel):
    CIS_MALE: int = 0
    CIS_FEMALE: int = 0
    TRANS_MALE: int = 0
    TRANS_FEMALE: int = 0
    OTHER: int = 0

class GroupByAgeGroup(BaseModel):
    sub_14: int = Field(0, alias="< 14")
    range_14_18: int = Field(0, alias="14 - 18")
    range_19_29: int = Field(0, alias="19 - 29")
    range_30_39: int = Field(0, alias="30 - 39")
    range_40_49: int = Field(0, alias="40 - 49")
    range_50_59: int = Field(0, alias="50 - 59")
    plus_60: int = Field(0, alias="> 60")

    class Config:
        allow_population_by_field_name = True

class GroupByMoment(BaseModel):
    true: int = Field(0, alias="True")
    false: int = Field(0, alias="False")

    class Config:
        allow_population_by_field_name = True

class GroupByMonths(BaseModel):
    Jan: int = 0
    Fev: int = 0
    Mar: int = 0
    Abr: int = 0
    Mai: int = 0
    Jun: int = 0
    Jul: int = 0
    Ago: int = 0
    Set: int = 0
    Out: int = 0
    Nov: int = 0
    Dez: int = 0

class GroupByNeighborhoods(BaseModel):
    name: str
    count: int