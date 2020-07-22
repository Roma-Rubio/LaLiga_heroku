mkdir -p ~/.streamlit/

echo “\
"general"\n\
email = \”romacencerrado@gmail.com\”\n\
“ > ~/.streamlit/credentials.toml

echo “\
"server"\nheadless = true\nenableCORS=false\nport = \n\
\n\
“ > ~/.streamlit/config.toml
