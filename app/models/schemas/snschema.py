from app.models.domain.snmodel import SNModel


class SNSchema(SNModel):
    class Config(SNModel.Config):
        orm_mode = True
