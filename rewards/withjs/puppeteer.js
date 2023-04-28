const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Navigate to https://rewards.bing.com/pointsbreakdown
  await page.goto('https://rewards.bing.com/pointsbreakdown');

  // Wait for the breakdown points to load
  await page.waitForSelector('.points-earned');
  
  // Extract the breakdown points
  const breakdownPoints = await page.evaluate(() => {
    const pointsEarned = document.querySelector('.points-earned').textContent;
    const pointsPending = document.querySelector('.points-pending').textContent;
    const pointsExpired = document.querySelector('.points-expired').textContent;
    return {
      pointsEarned,
      pointsPending,
      pointsExpired
    };
  });

  console.log(breakdownPoints);

  await browser.close();
})();
