openssl aes-256-cbc -K $encrypted_559225a2e7f0_key -iv $encrypted_559225a2e7f0_iv -in ./config.json.enc -out ./config.json -d
python -m pytest
