# Docker Quick Commands [DRAFT]


## List all container IDs

```sh
$ docker ps -a -q
4ff5324e9636
5f0cec9b5c71
e108bbf3ea22
a6a1d6306844
232642460fd7
b997d5016284
222a30c93694
31182cc11926
781e09ada5c7
9bffdfbb670e
43f6ba685883
02ab7c20e01d
35ee1033272c
0aa64438a0f8
909279a8c656
```

## Force stop/remove all containers

```sh
$ docker stop $(docker ps -a -q)

$ docker rm $(docker ps -a -q)
```


## Delete all unused containers/networks...

```sh
$ docker system prune

WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - all dangling build cache

Are you sure you want to continue? [y/N] y
Deleted Networks:
aa-bulk-grabber_default
aa-qa-bulk-e2e-test_default
aa_default

Deleted Images:
untagged: solomonxie/aa_ace_contest_201909@sha256:ac735b326b5303ad7cafcd54347e9eb1086e0935c9e85487d500c4350c80b114
deleted: sha256:56a191d08494a0b2b572345e5fce1ab966b32382ce13b345bbd35bda805cd9df
deleted: sha256:800a9f4654309621ac2bea04fff503ab5436ac505012d7f5f1bb9f6040459cc1
deleted: sha256:fb703a91d488d585a80ab6c9d358514a741b413a174fd6f9be28af3d896ccde7
deleted: sha256:638fa5563f49fe6f7ea1a0893fc89538cfffe359004ea1e595d8f1ea2f498d55
deleted: sha256:6c1ab126920007acc6ae7485a671d8be33b50c5961ed8cd9e33733e0da6e110c
deleted: sha256:c1938c54758090a0ada2d043c5fbac91aa45291aa7b0eb9fa8fd56b4256a6e65
```
