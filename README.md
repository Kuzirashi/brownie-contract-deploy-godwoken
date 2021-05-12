Prerequisites: 
- https://www.python.org/
- https://github.com/eth-brownie/brownie
- https://github.com/RetricSu/godwoken-kicker

Before running deploy add account and network to Brownie:
```
brownie accounts new 0 # and pass private key, this account needs to have CKB deposited on Layer 2 in Godwoken
yarn brownie:godwoken:add
```

Deploy:

```
git clone git@github.com:Kuzirashi/brownie-contract-deploy-godwoken.git
yarn
yarn build
yarn deploy:godwoken
```