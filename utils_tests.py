import pytest

from utils import get_block_txs


@pytest.fixture
def akashi_rest_url() -> str:
    return "https://api.akash.forbole.com:443"


@pytest.fixture
def akashi_non_empty_block_height() -> int:
    return 12100498


@pytest.mark.parametrize("block_height", [
    12100497,
    12100496,
    12100495
])
def test_get_empty_block_txs(akashi_rest_url, block_height):
    txs = get_block_txs(block_height, akashi_rest_url)
    assert len(txs) == 0


def test_get_not_empty_block_txs(akashi_rest_url, akashi_non_empty_block_height):
    txs = get_block_txs(akashi_non_empty_block_height, akashi_rest_url)
    assert len(txs) > 0

