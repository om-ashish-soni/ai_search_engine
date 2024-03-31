require('dotenv').config();
require('./page_pool')

const express = require('express');
const { search } = require('./search_engine');

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;



app.get('/ai/search', async (req, res) => {
    try {

        const { search_query, links_threshold = 5, data_limit_per_page = 10000 } = req.query;

        // console.log("search_query : ",search_query)
        // You can modify this based on your actual search logic
        const searchResult = await search(search_query, links_threshold, data_limit_per_page);

        // Respond with the search result
        return res.status(200).json({ success: true, data: searchResult });
    } catch (err) {
        console.log("Error while search : ", err);
        return res.status(400).json({ error: err.message })
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});