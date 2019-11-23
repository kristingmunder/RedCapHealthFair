openssl aes-256-cbc -K $encrypted_key -iv $encrypted_iv -in ./config.json.enc -out ./config.json -d
python -m pytest
