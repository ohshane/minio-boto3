# minio-boto3

```
docker run -p 9000:9000 -p 9001:9001 quay.io/minio/minio server /data --console-address ":9001"
```

modify default creds 'minioadmin:minioadmin' with env vars 'MINIO_ROOT_USER' and 'MINIO_ROOT_PASSWORD'.

MinIO Object Storage Server
Copyright: 2015-2023 MinIO, Inc.
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.html>
Version: RELEASE.2023-10-16T04-13-43Z (go1.21.3 linux/arm64)


Web GUI is provided @ 9001
```
S3-API: http://172.17.0.2:9000  http://127.0.0.1:9000
Console: http://172.17.0.2:9001 http://127.0.0.1:9001
```

<img width="1293" alt="image" src="https://github.com/ohshane/minio-boto3/assets/29338355/146cd968-3cc1-4415-bed4-ee671d44b9c3">
