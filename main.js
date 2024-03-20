import axios from 'axios';

const url = "https://arpeggi.io/api/kits/v1/voice-models";
const api_token = 'TSESMmZW.-Jb_8n6RnEzHPgiaGsw5gWFU';

const headers = {
    'Authorization': `Bearer ${api_token}`
};

const params = {
    order: 'asc',
    page: 1,
    perPage: 10,
    myModels: "true"
};

axios.get(url, { headers, params })
    .then(response => {
        console.log(JSON.stringify(response.data, null, 4));
    })
    .catch(error => {
        console.log("Something happened and there was an issue", error.message);
    });
