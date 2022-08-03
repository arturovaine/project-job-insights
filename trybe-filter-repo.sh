### GIT FILTER-REPO ###

## NÃO EXECUTE ESSE SCRIPT DIRETAMENTE
## Esse script foi feito para uso do
## script 'publisher.sh' fornecido 
## pela Trybe. 

[[ $# == 1 ]] && \
[[ $1 == "trybe-security-parameter" ]] && \
git filter-repo \
    --path .trybe \
    --path .github \
    --path .vscode \
    --path trybe.yml \
    --path trybe-filter-repo.sh \
    --path tests/test_flask_app.py \
    --path tests/test_insights.py \
    --path tests/test_jobs.py \
    --path tests/test_more_insights.py \
    --path tests/test_routes_and_views.py \
    --path tests/marker.py \
    --path tests/mocks* \
    --path tests/sorting/conftest.py \
    --path tests/sorting/mocks.py \
    --path tests/counter/conftest.py \
    --path tests/counter/mocks.py \
    --path tests/brazilian/conftest.py \
    --path tests/brazilian/mocks.py \
    --path .images \
    --path README.md \
    --invert-paths --force
