# tweepy-opensea-sales-bot
 
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!--[![LinkedIn][linkedin-shield]][linkedin-url]-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--<a href="https://github.com/ncvanegmond/tweet_opensea_sale_bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>-->

  <h3 align="center">Tweet Opensea Sale Bot</h3>

  <p align="center">
    Simple Tweepy bot that tweets out the most recent sale on OpenSea for a specific collection
    <br />
    <a href="https://github.com/ncvanegmond/tweet_opensea_sale_bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://twitter.com/CryptoTargetBot">View Demo</a>
    ·
    <a href="https://github.com/ncvanegmond/tweet_opensea_sale_bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/ncvanegmond/tweet_opensea_sale_bot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!--<li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>-->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Simple tweepy bot that will periodically call the Opensea API to check if there are new sales for a specific collection and tweets about it.

You can see it in action at [@CryptoTargetBot](https://twitter.com/CryptoTargetBot)

### Built With

* [Tweepy](https://www.tweepy.org/)
* [Opensea API](https://docs.opensea.io/reference/api-overview)




<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Read the docs on the [Opensea API](https://docs.opensea.io/reference/api-overview)
2. Clone the repo
   ```sh
   git clone https://github.com/ncvanegmond/tweet_opensea_sale_bot.git
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your Twitter API keys and OpenSea parameters in `.env`
   ```sh
   # Twitter keys
   API_KEY = xxx
   API_SECRET = xxx
   ACCESS_TOKEN = xxx
   ACCESS_TOKEN_SECRET = xxx
   # OpenSea collection parameters
   COLLECTION_SLUG = marscatsvoyage
   CONTRACT_ADDRESS = 0xdd467a6c8ae2b39825a452e06b4fa82f73d4253d
   OPENSEA_SHARED_STOREFRONT_ADDRESS = 0x495f947276749Ce646f68AC8c248420045cb7b5e
   ```



<!-- USAGE EXAMPLES -->
<!--## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_-->



<!-- ROADMAP -->
<!--## Roadmap

See the [open issues](https://github.com/ncvanegmond/tweet_opensea_sale_bot/issues) for a list of proposed features (and known issues).-->



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Niels van Egmond - [@ncvanegmond](https://twitter.com/ncvanegmond)

Project Link: [https://github.com/ncvanegmond/tweet_opensea_sale_bot](https://github.com/ncvanegmond/tweet_opensea_sale_bot)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Miguel Garcia's 'How to make a Twitter bot in Python with Tweepy'](https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ncvanegmond/tweet_opensea_sale_bot.svg?style=for-the-badge
[contributors-url]: https://github.com/ncvanegmond/tweet_opensea_sale_bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ncvanegmond/tweet_opensea_sale_bot.svg?style=for-the-badge
[forks-url]: https://github.com/ncvanegmond/tweet_opensea_sale_bot/network/members
[stars-shield]: https://img.shields.io/github/stars/ncvanegmond/tweet_opensea_sale_bot.svg?style=for-the-badge
[stars-url]: https://github.com/ncvanegmond/tweet_opensea_sale_bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/ncvanegmond/tweet_opensea_sale_bot.svg?style=for-the-badge
[issues-url]: https://github.com/ncvanegmond/tweet_opensea_sale_bot/issues
[license-shield]: https://img.shields.io/github/license/ncvanegmond/tweet_opensea_sale_bot.svg?style=for-the-badge
[license-url]: https://github.com/ncvanegmond/tweet_opensea_sale_bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png