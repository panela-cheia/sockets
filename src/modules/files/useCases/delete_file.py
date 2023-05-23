from modules.files.repositories.files_repository import FilesRepository
from modules.files.dtos.delete_file_dto import DeleteFileDTO

from shared.errors.errors import CustomError

class DeleteFileUseCase:
    def __init__(self, repository: FilesRepository) -> None:
        self.repository = repository

    async def execute(self, deleteFileDTO:DeleteFileDTO):

        verifyIfFileExists = await self.repository.findById(id=deleteFileDTO.id)

        if not verifyIfFileExists:
            raise CustomError("File not found")
        
        try:
            return await self.repository.delete(deleteFileDTO.id)
        except:
            raise Exception("An error occurred during file deletion")