const { chromium } = require('playwright');
// const puppeteer = require('puppeteer');

const pagePoolSize = process.env.PAGE_POOL_SIZE;

let browser = null;
let pagePool = [];

// each pagePool contains object of type : { ready:'true/false',page:pageObject}

/**
 * 
 * @returns browserContext
 */
const launchBrowser = async () => {
    if (browser) return browser;
    // const newBrowser = await puppeteer.launch({
    //     headless: "new"
    // })
    const newBrowser = await chromium.launch({ headless: true });
    browserContext = await newBrowser.newContext();
    console.log(`Launching new browser`)
    return newBrowser;
}

const launchNewPage = async () => {
    // console.log(`Rendering new browser page`)
    browser = await launchBrowser();
    return await browser.newPage()
}

const pickReadyPage = () => {
    const foundIndex = pagePool.findIndex(pageObject => pageObject.ready)
    if (foundIndex == -1) return null;
    console.log(`Pickedup Ready Page with index : ${foundIndex}`)
    pagePool[foundIndex].ready = false;
    return pagePool[foundIndex].page;
}


const putBackReadyPage=(freshPage)=>{
    const foundIndex = pagePool.findIndex(pageObject => !pageObject.ready)
    if (foundIndex == -1) return;
    console.log(`Putting Back Ready Page with index : ${foundIndex}`)
    pagePool[foundIndex].ready = true;
    pagePool[foundIndex].page=freshPage;
}


/**
 * 
 * @returns browser page
 */
const renderPage = async () => {
    try{
        const foundPage = pickReadyPage();
        if (foundPage) return foundPage;
        return await launchNewPage();
    }catch(err){
        console.log("error while rendering page : ",err);
    }
    
}

const cleanPage = async (page) => {
    console.log(`going to clean the page`)
    await page.setContent('');
    console.log(`Cleaned page`)
    return page;
}

const returnPage = async (page) => {
    try{
        const freshPage=await cleanPage(page);
        putBackReadyPage(freshPage);
    }catch(err){
        console.log("Error while returning page : ",err);
    }
}

const initializePagePool = async () => {
    try {

        // console.log(`Entry initializePagePool`)
        const startTime = performance.now();

        pagePool = [];

        browser = await launchBrowser();

        const readyPagePromises = [];
        for (let i = 0; i < pagePoolSize; i++) {
            readyPagePromises.push(
                launchNewPage()
            )
            pagePool.push(
                {
                    ready: false,
                    page: null
                }
            )
        }

        const readyPages = await Promise.all(readyPagePromises);

        for (let i = 0; i < pagePoolSize; i++) {
            pagePool[i].ready = true;
            pagePool[i].page = readyPages[i];
        }

        console.log(`PagePool is ready : ${(performance.now() - startTime).toFixed(2)} milliseconds`)
        // console.log(`Exit from initializePagePool`)
    } catch (err) {
        console.log("Error while initializing pagePool : ", err);
    }

}

setImmediate(()=>{
    initializePagePool()
})

module.exports = {
    renderPage:renderPage,
    returnPage:returnPage,
}