https://velog.io/@roong-ra/Git-%EC%97%90%EB%9F%AC-Fatal-%EC%A0%95%EB%B0%A9%ED%96%A5%EC%9D%B4-%EB%B6%88%EA%B0%80%EB%8A%A5%ED%95%98%EB%AF%80%EB%A1%9C-%EC%A4%91%EC%A7%80%ED%95%A9%EB%8B%88%EB%8B%A4



https://synapsis9.tistory.com/entry/git-pull-%EA%B2%BD%EA%B3%A0%EC%97%86%EC%95%A0%EA%B8%B0-Pulling-without-specifying-how-to-reconcile-divergent-branches-is-discouraged



해결법
해당 레포지토리만 silence 하려면

git config pull.ff only
향후 모든 레포지토리에 대해 적용하려면

git config --global pull.ff only