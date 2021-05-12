```
➜  $ brownie networks add Godwoken-Dev godwokendev host=http://localhost:8024 chainid=0x3
Brownie v1.14.6 - Python development framework for Ethereum

SUCCESS: A new network 'godwokendev' has been added
  └─godwokendev
    ├─id: godwokendev
    ├─chainid: 0x3
    └─host: http://localhost:8024
```

brownie run scripts/deploy --network godwokendev