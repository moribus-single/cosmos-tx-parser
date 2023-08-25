import base64
import json

from cosmpy.common.rest_client import RestClient


def get_block_txs(block_height, rest_address):
    """Get block transactions by block height in akash network"""
    # initialize rest client
    rest_client = RestClient(rest_address)

    # get response
    resp = rest_client.get(f"/blocks/{block_height}")

    # validate response for converting into dict
    valid_resp = resp.decode("utf-8").replace("'", '"')
    data = json.loads(valid_resp)

    # obtain transactions list
    # and decode with base64
    txs = data["block"]["data"]["txs"]
    return [base64.b64decode(t) for t in txs]
