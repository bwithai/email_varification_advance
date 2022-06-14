from fastapi import HTTPException, status


duplicate_record_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Record already exists.",
    headers={"WWW-Authenticate": "Bearer"},
)

expired_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Token expired'
)

invalid_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Invalid token'
)

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Record not found"
)
