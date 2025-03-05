from ddmail_validators.validators import is_username_allowed, is_email_allowed, is_domain_allowed, is_password_allowed, is_account_allowed, is_sha256_allowed, is_mx_valid, is_spf_valid, is_dkim_valid, is_dmarc_valid, is_openpgp_public_key_allowed, is_openpgp_key_fingerprint_allowed, is_openpgp_keyring_allowed


def test_is_username_allowed():
    assert is_username_allowed("A") is True
    assert is_username_allowed("1") is True
    assert is_username_allowed("A2B83") is True
    assert is_username_allowed("a2B83") is False
    assert is_username_allowed("A2b83") is False
    assert is_username_allowed("A2B#83") is False
    assert is_username_allowed("A2B8=3") is False
    assert is_username_allowed("A2B83;") is False
    assert is_username_allowed("A2B8_3") is False
    assert is_username_allowed("-A2B83") is False
    assert is_username_allowed("\"A2B83") is False


def test_is_password_allowed():
    assert is_password_allowed("a2A83") is True
    assert is_password_allowed("1a2A835") is True
    assert is_password_allowed("F1a2A835V") is True
    assert is_password_allowed("as3dgD5khjFgsad6Gjgb6") is True
    assert is_password_allowed("aA8/+=\\") is False
    assert is_password_allowed("aA8/+=\\vfgg") is False
    assert is_password_allowed("aAx\"fds") is False
    assert is_password_allowed("a-b3") is False
    assert is_password_allowed("a--b3") is False
    assert is_password_allowed("a<b3") is False
    assert is_password_allowed("a>b5") is False
    assert is_password_allowed("a>>6") is False
    assert is_password_allowed("as3dgD5khjFgsad6Gj_gb6") is False
    assert is_password_allowed("as3dgD5khjF#gsad6Gjgb6") is False
    assert is_password_allowed("as3dgD5<khjFgsad6Gjgb6") is False
    assert is_password_allowed("as3dgD5>khjFgsad6Gjgb6") is False
    assert is_password_allowed("as3dgD5-khjFgsad6Gjgb6") is False
    assert is_password_allowed("as3dgD5--khjFgsad6Gjgb6") is False
    assert is_password_allowed("as3dgD5@khjFgsad6Gjgb6") is False
    assert is_password_allowed("as3dgD5|khjFgsad6Gjgb6") is False
    assert is_password_allowed("as3dg;D5khjFgsad6Gjgb6") is False


def test_is_domain_allowed():
    assert is_domain_allowed("test.se") is True
    assert is_domain_allowed("testtes-t.se") is True
    assert is_domain_allowed("t.s") is False
    assert is_domain_allowed("test.se.") is False
    assert is_domain_allowed("te_st.se") is False
    assert is_domain_allowed(".test@test.se") is False
    assert is_domain_allowed("t@est.se") is False
    assert is_domain_allowed("test.test.se@") is False
    assert is_domain_allowed("testte<>st.se") is False
    assert is_domain_allowed("te>sttest.se") is False
    assert is_domain_allowed("te<test.se") is False
    assert is_domain_allowed("te=sttest.se") is False
    assert is_domain_allowed("test=t.se") is False
    assert is_domain_allowed("testtest..se") is False
    assert is_domain_allowed("t\"est@test.se") is False


def test_is_email_allowed():
    assert is_email_allowed("test@test.se") is True
    assert is_email_allowed("test@tes-t.se") is True
    assert is_email_allowed("test@tes_t.se") is False
    assert is_email_allowed("t@t.s") is False
    assert is_email_allowed("test@test.se.") is False
    assert is_email_allowed(".test@test.se") is False
    assert is_email_allowed("@test.se") is False
    assert is_email_allowed("test.test.se@") is False
    assert is_email_allowed("test@te<>st.se") is False
    assert is_email_allowed("te>st@test.se") is False
    assert is_email_allowed("te<st@test.se") is False
    assert is_email_allowed("te=st@test.se") is True
    assert is_email_allowed("test@tes=t.se") is False
    assert is_email_allowed("test@test..se") is False
    assert is_email_allowed("t\"est@test.se") is False


def test_is_account_allowed():
    assert is_account_allowed("DEV") is True
    assert is_account_allowed("A1B2C3") is True
    assert is_account_allowed("AbC") is False
    assert is_account_allowed("A#BC") is False
    assert is_account_allowed("A>BC") is False
    assert is_account_allowed("A;BC") is False
    assert is_account_allowed("A.BC") is False
    assert is_account_allowed("A,BC") is False
    assert is_account_allowed("A-BC") is False
    assert is_account_allowed("A_BC") is False


def test_is_mx_valid():
    assert is_mx_valid("crew.ddmail.se", "mail.ddmail.se.", "10") is True
    assert is_mx_valid("drz.se", "mail.ddmail.se.", "10") is False


def test_is_spf_valid():
    assert is_spf_valid("crew.ddmail.se", '"v=spf1 mx -all"') is True
    assert is_spf_valid("drz.se", '"v=spf1 mx -all"') is False


def test_is_dkim_valid():
    dkim_record = '"v=DKIM1; k=rsa;  \\009p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoxbFCUM83lUvHKku3mE/IOb2LArgPsjzhijO4pZfVLrLp7dv8RKDs4MmtFHrdWf4UibDFZtPm4IKcagDD3LlqgPSeewnfesI/kGCdz2SqPA/R5Cip5I1swtQ1lKa41eu6Rxym32fzCrRAhBfOZqM05BKPQQpxcSuyNmKOz+HGlGtkUMk5ebhWDtTsoc7ntw" "nhnAxaF+T61YQdYyCL \\009P7l6KRULaDJ3U7AkNAYrXpv0AdfjDVZp+GXu5fqTFTMi5pYGv1pj4621OSysDmjFlPksCgDouE11N+sJVCVPj//8gJCpzDv7y2kET9MIPmIlKGBTC1AQg5KWrbkeQPcEnzhRwIDAQAB"'

    assert is_dkim_valid("crew.ddmail.se", dkim_record) is True
    assert is_dkim_valid("drz.se", dkim_record) is False


def test_is_dmarc_valid():
    dmarc_record = '"v=DMARC1; p=none"'

    assert is_dmarc_valid("crew.ddmail.se", dmarc_record) is False
    assert is_dmarc_valid("drz.se", dmarc_record) is True


def test_is_openpgp_public_key_allowed():
    assert is_openpgp_public_key_allowed("-----BEGIN PGP PUBLIC KEY BLOCK-----abcABC012=/+-----END PGP PUBLIC KEY BLOCK-----") is True
    assert is_openpgp_public_key_allowed("-----BEGIN PGP PUBLIC KEY BLOCK-----abc;ABC012=/+-----END PGP PUBLIC KEY BLOCK-----") is False
    assert is_openpgp_public_key_allowed("-----BEGIN PGP PUBLIC KEY BLOCK------abcABC012=/+-----END PGP PUBLIC KEY BLOCK-----") is False
    assert is_openpgp_public_key_allowed("-----BEGIN PGP PUBLIC KEY BLOCK-----\"abcABC012=/+-----END PGP PUBLIC KEY BLOCK-----") is False
    assert is_openpgp_public_key_allowed("-----BEGIN PGP PUBLIC KEY BLOCK-----a:bcABC012=/+-----END PGP PUBLIC KEY BLOCK-----") is False
    assert is_openpgp_public_key_allowed("----BEGIN PGP PUBLIC KEY BLOCK-----abcABC012=/+-----END PGP PUBLIC KEY BLOCK-----") is False
    assert is_openpgp_public_key_allowed("-----BEGIN PGP PUBLIC KEY BLOCK-----abcABC012=/+-----END PGP PUBLIC KEY BLOCK------") is False


def test_is_openpgp_key_fingerprint_allowed():
    assert is_openpgp_key_fingerprint_allowed("EF6E286DDA85EA2A4BA7DE684E2C6E8793298290") is True
    assert is_openpgp_key_fingerprint_allowed("EF6E286DDA85EA2A4BA7DE684E2C6E8793298290A") is False
    assert is_openpgp_key_fingerprint_allowed("F6E286DDA85EA2A4BA7DE684E2C6E8793298290") is False
    assert is_openpgp_key_fingerprint_allowed("EF6E286DDA85EA2A4:A7DE684E2C6E8793298290") is False
    assert is_openpgp_key_fingerprint_allowed("E;6E286DDA85EA2A4BA7DE684E2C6E8793298290") is False


def test_is_openpgp_keyring_allowed():
    assert is_openpgp_keyring_allowed("ABC012") is True
    assert is_openpgp_keyring_allowed("aBC012") is False
    assert is_openpgp_keyring_allowed("A:BC012") is False
    assert is_openpgp_keyring_allowed("AB;C012") is False
    assert is_openpgp_keyring_allowed("ABC$012") is False
    assert is_openpgp_keyring_allowed("ABC0@12") is False
    assert is_openpgp_keyring_allowed("ABC0&12") is False


def test_is_sha256_allowed():
    assert is_sha256_allowed("7b7632005be0f36c5d1663a6c5ec4d13315589d65e1ef8687fb4b9866f9bc4b0") is True
    assert is_sha256_allowed("") is False
    assert is_sha256_allowed("a1d4") is False
    assert is_sha256_allowed("a1b2") is False
    assert is_sha256_allowed("7b7632005be0f36c5d1663a6c5ec4d13315589d65e1ef8687fb4b9866f9bc4b0a") is False
    assert is_sha256_allowed("7b7632005be0f36c5d1663a6c5ec4d13315589d651ef8687fB4b9866f9bc4b0") is False
    assert is_sha256_allowed("7b7632005b.0f36c5d1663a6c5ec4d13315589d65e1ef8687fb4b9866f9bc4b0") is False
    assert is_sha256_allowed("7b7632005be\"f36c5d1663a6c5ec4d13315589d65e1ef8687fb4b9866f9bc4b0") is False
    assert is_sha256_allowed("7b7632005be-f36c5d1663a6c5ec4d13315589d65e1ef8687fb4b9866f9bc4b0") is False
    assert is_sha256_allowed("7b7632005b.0f36c5d1663a6c5ec4d13315589d65e1ef8687fb4b9866f9bc4b0") is False
