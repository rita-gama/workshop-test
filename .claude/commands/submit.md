Submete a solução deste exercício:

1. Faz `git add -A`, `git commit -m "submission"` e `git push`.
2. Espera 5 segundos e obtém o ID da execução mais recente com:
   `gh run list --limit 1 --json databaseId --jq '.[0].databaseId'`
3. Acompanha essa execução com `gh run watch <ID> --exit-status`.
4. Diz-me se passou ou falhou. Se falhou, corre `gh run view <ID> --log-failed`
   e explica qual teste falhou e porquê, sem me dar a solução.