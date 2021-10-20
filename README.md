# Jump App Protobuf files

This repository contains protocol buffer language files in order to share these resources for every _Jump App_ gRPC microservice.

## Compile

```
protoc --go_out=. --go_opt=paths=source_relative  --go-grpc_out=. --go-grpc_opt=paths=source_relative jump/jump.proto
```
