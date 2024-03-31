require('dotenv').config();

// const { chromium } = require('playwright');
const cheerio = require('cheerio');
const { renderPage } = require('./page_pool');
const WEB_STORE = process.env.WEB_STORE;


/**
 * 
 * @param {string} url 
 * @returns {boolean} true/false - whether url is valid or not
 */
function isValidUrl(url) {
  const pattern = /^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/gm;
  return pattern.test(url);
}

/**
 * 
 * @param {string} inputString 
 * @returns {string} outputString with removed whitespaces
 */
function removeWhitespaceAndJoin(inputString) {
  const stringWithoutWhitespace = inputString.replace(/\s/g, ''); // Replace whitespace with ''
  const finalString = stringWithoutWhitespace.split('›').join('/'); // Split by '>' and join by ''
  return finalString;
}

/**
 * 
 * @param {string} inputString 
 * @returns 
 */
function removeSubstringsBetweenAngles(inputString) {
  // Regular expression to match substrings between '<' and '>'
  const regex = /<[^>]*>/g;

  // Replace matched substrings with an empty string
  const stringWithoutSubstrings = inputString.replace(regex, '');

  return stringWithoutSubstrings;
}


/**
 * 
 * @param {string} htmlString 
 * @returns {string} - extracted text from html
 */
function extractTextFromHTML(htmlString) {

  const noStyleHtml = htmlString.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');

  // Remove <script> tags and their content
  const noScriptHtml = noStyleHtml.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');

  let $ = cheerio.load(noScriptHtml);

  // Remove content between <style> and </style> tags
  $('style').remove();

  // Remove content between <script> and </script> tags
  $('script').remove();

  // Remove inline style attributes
  $('[style]').removeAttr('style');


  // console.log("after removing see html : ",$.html().substring(0,2000))
  // Use .text() method to get the combined text from all elements
  let extractedText = $.text().trim();

  extractedText = extractedText.replace(/{[^}]+}/g, '');

  // Remove extra white spaces (spaces, tabs, line breaks)
  extractedText = extractedText.replace(/\s+/g, ' ');

  return extractedText.trim();
}


/**
 * 
 * @param {string} linkUrl 
 * @param {number} data_limit_per_page 
 * @returns {string} data on the given web source
 */
const retrive_data_from_web_page = async (linkUrl,data_limit_per_page) => {
  // const page = await context.newPage();
  const page = await renderPage();
  try{
    await page.goto(linkUrl,timeout=100_000);
  }catch(err){
    return '';
  }
  
  const pageContent = await page.textContent('body');

  // Log the text content of the page
  const textContent = extractTextFromHTML(pageContent).trim().substring(0, data_limit_per_page)
  return textContent;
}

/**
 * 
 * @param {number} links_threshold 
 * @param {number} data_limit_per_page 
 * @returns {Promise<Object.<string, string>>} search_result - a map containing key:linkUrl, value:data
 */
const search = async (search_query, links_threshold, data_limit_per_page = 10000,retried=false) => {
  
  const search_result = {};
  // Launch the browser
  // const browser = await chromium.launch({ headless: false });
  // const context = await browser.newContext();
  // const page = await context.newPage();
  const page = await renderPage();

  const textareaSelector = 'textarea'; // Update this to your textarea selector

  await page.goto(WEB_STORE,timeout=100_000);

  await page.focus(textareaSelector);
  await page.keyboard.type(search_query);

  // Simulate hitting the "Enter" key
  await page.keyboard.press('Enter');


  await new Promise(resolve => setTimeout(resolve, 2000))

  const linkElements = await page.$$('span a');

  
  const all_links = []
  for (const linkElement of linkElements) {
    const hrefValue = await linkElement.getAttribute('href');
    

    // const textContent = await linkElement.innerText();
    // console.log("textContent : ",textContent);
    // const linkUrl = removeWhitespaceAndJoin(textContent)
    const linkUrl = hrefValue;

    const isValid = isValidUrl(linkUrl)
    if (isValid) {
      if (all_links.length < links_threshold) {
        all_links.push(linkUrl);
      }
      else break;
    }
  }
  // console.log("all_links : ", all_links)


  const pagesContent = []
  const all_data_promises = [];
  for (let linkUrl of all_links) {
    all_data_promises.push(
      retrive_data_from_web_page(linkUrl,data_limit_per_page)
    )

  }

  const all_data=await Promise.all(all_data_promises);

  for(let link_index=0;link_index<all_links.length;link_index++){
    const curr_link=all_links[link_index]
    const curr_data=all_data[link_index]
    search_result[curr_link]=curr_data;
  }

  return search_result;

}


// (async () => {
//   // Example usage:
//   //   const htmlString = `
//   // <div>
//   //   This is <b>bold</b> and <i>italic</i>.
//   //   <style>
//   //     body {
//   //       background-color: lightblue;
//   //     }
//   //   </style>
//   //   <script>
//   //     alert("Hello!");
//   //   </script>

//   //   <script>
//   //   {"topSectionLinks":[{"title":"Home","url":"/","navbarId":"HOME"},{"title":"Gam
//   // es & Quizzes","url":"/quiz/browse","navbarId":"QUIZZES"}
//   //   </script>
//   //   <p>Paragraph with <a href="#">link</a>.</p>
//   // </div>
//   // `;

//   //   const extractedText = extractTextFromHTML(htmlString);
//   //   console.log(extractedText);

//   const search_result = await search("Who is Sundar Pichai", 3)
//   console.log("search_result : ", search_result)
// })()


module.exports={
  search:search
}
