#!/usr/bin/env python
import argparse
import os
import M2Crypto
from M2Crypto.util import no_passphrase_callback
from jwkest.jwk import dump_jwk

__author__ = 'rolandh'

def create_and_store_rsa_key_pair(name="pyoidc", path=".", size=1024):
    #Seed the random number generator with 1024 random bytes (8192 bits)
    M2Crypto.Rand.rand_seed(os.urandom(size))

    key = M2Crypto.RSA.gen_key(size, 65537, lambda : None)

    if not path.endswith("/"):
        path += "/"

    key.save_key('%s%s' % (path, name), None, callback=no_passphrase_callback)
    key.save_pub_key('%s%s.pub' % (path, name))

    jwk_spec = dump_jwk([key], "enc")

    f = open("%s%s.jwk" % (path, name), "w")
    f.write(jwk_spec)
    f.close()

    return key

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest="name", default="pyoidc",
                        help="file names")
    parser.add_argument('-p', dest="path", default=".",
                        help="Path to the directory for the files")
    parser.add_argument('-s', dest="size", default=1024,
                        help="Key size", type=int)

    args = parser.parse_args()

    create_and_store_rsa_key_pair(args.name, args.path, args.size)