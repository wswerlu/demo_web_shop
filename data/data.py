from mimesis.enums import CardType

PRODUCTS_WITHOUT_ATTRIBUTES = [
    'computing-and-internet',
    'fiction',
    'health',
    'copy-of-tcp-self-paced-training-2',
    'copy-of-copy-of-copy-of-copy-of-tcp-self-paced-training',
    'copy-of-tcp-self-paced-training',
    'copy-of-copy-of-copy-of-tcp-self-paced-training',
    'tcp',
    'copy-of-tcp-self-paced-training-3',
    'smartphone',
    'blue-jeans',
    'casual-belt',
    'genuine-leather-handbag-with-cell-phone-holder-many-pockets',
    'album-3',
    'music-album-1',
    'music-2',
    'black-white-diamond-heart',
]

CREDIT_CARD_TYPE = {
    'Visa': CardType.VISA,
    'Master card': CardType.MASTER_CARD,
    'Amex': CardType.AMERICAN_EXPRESS,
    'Discover': None,
}
