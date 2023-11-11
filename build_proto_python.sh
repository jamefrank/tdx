#!/bin/bash
protoc -I=./protos --python_out=./ --mypy_out=./ ./protos/tdx_tools/protos/*.proto
