from passlib.context import CryptContext

#
# import the CryptContext class, used to handle all hashing...
#
from passlib.context import CryptContext

#
# create a single global instance for your app...
#
pwd_context = CryptContext(
    # Replace this list with the hash(es) you wish to support.
    # this example sets pbkdf2_sha256 as the default,
    # with additional support for reading legacy des_crypt hashes.
    schemes=["pbkdf2_sha256", "des_crypt"],
    # Automatically mark all but first hasher in list as deprecated.
    # (this will be the default in Passlib 2.0)
    deprecated="auto",
    # Optionally, set the number of rounds that should be used.
    # Appropriate values may vary for different schemes,
    # and the amount of time you wish it to take.
    # Leaving this alone is usually safe, and will use passlib's defaults.
    pbkdf2_sha256__rounds=29000,
)


class Mypasslib:
    def encrypt_password(self, password):
        return pwd_context.hash(password)

    def check_encrypted_password(self, password, hashed):
        return pwd_context.verify(password, hashed)
