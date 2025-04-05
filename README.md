<h1 align="center">Metrix</h1>
<p align="center">Metrix generates a customizable retro-style GIF showcasing GitHub metrics for your GitHub README profile.</p>

<table align="center">
  <tr>
    <td align="center">
      <a href="#default"><img src="img/metrix-default.gif" width="240px" /></a>
    </td>
    <td align="center">
      <a href="#red"><img src="img/metrix-red.gif" width="240px" /></a>
    </td>
    <td align="center">
      <a href="#blue"><img src="img/metrix-blue.gif" width="240px" /></a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="#default"><b>Default</b></a>
    </td>
    <td align="center">
      <a href="#red"><b>Red</b></a>
    </td>
    <td align="center">
      <a href="#blue"><b>White-Blue</b></a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="#yellow-noglitch"
        ><img src="img/metrix-yellow-noglitch.gif" width="240px"
      /></a>
    </td>
    <td align="center">
      <a href="#gold-customtext"
        ><img src="img/metrix-gold-customtext.gif" width="240px"
      /></a>
    </td>
    <td align="center">
      <a href="#purple-torvalds"
        ><img src="img/metrix-purple-torvalds.gif" width="240px"
      /></a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="#yellow-noglitch"><b>Yellow No-Glitch</b></a>
    </td>
    <td align="center">
      <a href="#gold-customtext"><b>Gold Custom Text</b></a>
    </td>
    <td align="center">
      <a href="#purple-torvalds"><b>Purple Torvalds</b></a>
    </td>
  </tr>
</table>

## Usage Guide

Follow these steps to integrate Metrix into your GitHub profile:

1. **Create a New Repository**  
   Create a new repository to host your profile README. For guidance, refer to GitHub’s documentation on [setting up and managing your profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme).

2. **(Optional) Generate and Add a Personal Access Token (PAT)**  
   By default, the action will only display public data. To also include private repository data, follow these steps:

   1. Create a PAT token from [GitHub's Token Settings](https://github.com/settings/tokens) with the following permissions:

      - **repo**: Full control of private repositories
      - **read:org**: Read org and team membership, and org projects
      - **read:user**: Read all user profile data

   2. In your repository, navigate to **Settings > Secrets and variables** and add a new secret:

      - Name the secret `PAT_TOKEN`
      - Paste the PAT token value generated in the previous step

3. **Enable Workflow Permissions**  
   In your repository settings, go to **Settings > Actions > General** and enable **"Read repository contents and packages permissions"** at the bottom of the page.

4. **Add the Metrix GIF to Your README**  
   Add the following to your `README.md` file:

   ```markdown
   ![metrix](metrix.gif)
   ```

5. **Create a GitHub Action**  
   In your repository, create a new GitHub Action by copying the contents of the [metrix-basic.yml](.github/workflows/metrix-basic.yml) file.

6. **Run the Action**  
   Your action is now set up! Commit the changes and manually trigger the action to generate the metrics GIF.

7. **(Optional) Customize your Metrix**  
   You can use the [metrix-complete.yml](.github/workflows/metrix-complete.yml) file or read the [parameters](#parameters) section to find some parameters to add and customize in your action.

## Showcase

Some examples are provided below, with the corresponding configuration for each:

---

### <a id="default"></a> Default

> Notice that looping is deactivated by default!

![default](img/metrix-default.gif)

```
with:
  GITHUB_USERNAME: 'joanroig'
```

---

### <a id="red"></a> Red

![red](img/metrix-red.gif)

```
with:
  GITHUB_USERNAME: 'joanroig'
  TEXT_COLOR: 'red'
  LOOP: 'true'
```

---

### <a id="blue"></a> White over blue

![blue](img/metrix-blue.gif)

```
with:
  GITHUB_USERNAME: 'joanroig'
  TEXT_COLOR: 'white'
  BACKGROUND_COLOR: 'blue'
  LOOP: 'true'
```

---

### <a id="yellow-noglitch"></a> Yellow with disabled glitches

![yellow noglitch](img/metrix-yellow-noglitch.gif)

```
with:
  GITHUB_USERNAME: 'joanroig'
  TEXT_COLOR: 'yellow'
  GLITCHES: 'false'
  LOOP: 'true'
```

---

### <a id="gold-customtext"></a> Gold over dark gold, with custom texts

![gold customtext](img/metrix-gold-customtext.gif)

```
with:
  GITHUB_USERNAME: 'joanroig'
  TEXT_COLOR: 'gold'
  BACKGROUND_COLOR: 'darkgoldenrod'
  TITLE_SUFFIX: ' is booting up......'
  ACTIVITY_TEXT: 'I worked a lot lately...'
  LOOP: 'true'
```

---

### <a id="purple-torvalds"></a> Yellow over purple, with data from another user, reduced activity days, and custom activity text

![default](img/metrix-purple-torvalds.gif)

```
with:
  GITHUB_USERNAME: 'torvalds'
  TEXT_COLOR: 'yellow'
  BACKGROUND_COLOR: 'purple'
  ACTIVITY_TEXT: 'Last two weeks were intense:'
  ACTIVITY_DAYS: '14'
  LOOP: 'true'
```

---

## <a id="parameters"></a>Available Parameters and Options

Metrix is highly customizable through GitHub Action arguments. A complete example, including the default parameters, is provided: [metrix-complete.yml](.github/workflows/metrix-complete.yml). Below is the full list of available parameters:

| **Category**         | **Parameter**      | **Description**                                                                                                        | **Example/Options**                                                                                 |
| -------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Authentication**   | GITHUB_TOKEN       | GitHub token used for authentication. Defaults to `PAT_TOKEN` if available.                                            | `${{ secrets.PAT_TOKEN \|\| secrets.GITHUB_TOKEN }}`                                                |
|                      | GITHUB_USERNAME    | GitHub username to display the metrics for.                                                                            | `${{ github.actor }}`                                                                               |
| **Font Settings**    | FONT_SIZE          | Font size for the main text.                                                                                           | `'20'`                                                                                              |
|                      | SYMBOL_FONT_SIZE   | Font size for symbols.                                                                                                 | `'20'`                                                                                              |
|                      | FONT_PATH          | Path to the primary font file.                                                                                         | `'assets/MxPlus_IBM_BIOS.ttf'`                                                                      |
|                      | SYMBOL_FONT_PATH   | Path to the symbol font file.                                                                                          | `'assets/MxPlus_IBM_BIOS.ttf'`                                                                      |
| **Color Settings**   | TEXT_COLOR         | Color of the text. Options include CSS color names, hex codes, or 'random', 'complementary', 'contrasting' or 'shade'. | `'blue'`,`'#c4a5a3'`,`'random'`, `'complementary'`, `'contrasting'`, `'shade'`, etc                 |
|                      | BACKGROUND_COLOR   | Background color. Same options as TEXT_COLOR.                                                                          | `'red'`,`'#6e2e2a'`,`'random'`, `'complementary'`, `'contrasting'`, `'shade'`, etc                  |
|                      | MINIMUM_CONTRAST   | Minimum contrast ratio between text and background (1 to 21).                                                          | `'2'`                                                                                               |
| **Content Settings** | TEXT               | Text content for the Metrix display. Use variables for dynamic data. See [Text Variables](#variables) below.           | `'My name is {username}`<br>`I love {preferred_languages[1]},`<br>`and I have {total_stars} stars'` |
|                      | TYPING_CHARACTER   | Character used for the typing effect.                                                                                  | `'█'`                                                                                               |
|                      | ACTIVITY_TEXT      | Text to display for the activity section.                                                                              | `'Last month commit activity:'`                                                                     |
|                      | ACTIVITY_DAYS      | Number of days for the activity chart.                                                                                 | `'30'`                                                                                              |
| **Display Settings** | FPS                | Frames per second for the GIF.                                                                                         | `'50'`                                                                                              |
|                      | LOOP               | Enable or disable infinite looping of the GIF.                                                                         | `'true'` or `'false'`                                                                               |
|                      | WIDTH              | Width of the generated GIF.                                                                                            | `'622'`                                                                                             |
|                      | HEIGHT             | Height of the generated GIF.                                                                                           | `'356'`                                                                                             |
| **Glitch Effects**   | GLITCHES           | Enable or disable glitches in the GIF.                                                                                 | `'true'` or `'false'`                                                                               |
|                      | MAX_GLITCHES       | Maximum number of glitches that can occur simultaneously.                                                              | `'4'`                                                                                               |
|                      | GLITCH_PROBABILITY | Probability of a glitch occurring in a frame (0 to 100).                                                               | `'3'`                                                                                               |
| **Output Settings**  | OUTPUT_FILE_PATH   | Path for the generated GIF.                                                                                            | `'metrix.gif'`                                                                                      |

### <a id="variables"></a>Text Variables (Curated GitHub API Data)

| **Variable**                                          | **Description**                                                                      | **Example Replacement**            |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------- |
| `{username}`                                          | GitHub username                                                                      | `'joanroig'`                       |
| `{separator}`                                         | Custom separator for formatting                                                      | `'------------------------------'` |
| `{updated_date}`                                      | Date of the latest update                                                            | `'2025-04-05'`                     |
| `{total_repos}`                                       | Total number of repositories                                                         | `'42'`                             |
| `{total_commits}`                                     | Total number of commits                                                              | `'500'`                            |
| `{total_stars}`                                       | Total number of stars across repositories                                            | `'150'`                            |
| `{total_forks}`                                       | Total number of forks                                                                | `'30'`                             |
| `{total_watchers}`                                    | Total number of watchers                                                             | `'100'`                            |
| `{total_open_issues}`                                 | Total number of open issues                                                          | `'10'`                             |
| `{preferred_languages}` or `{preferred_languages[X]}` | Preferred programming languages, where X can be set to a number to limit the results | `'TypeScript, Python, JavaScript'` |
| `{preferred_topics}` or `{preferred_topics[X]}`       | Preferred topics, where X can be set to a number to limit the results                | `'API, Hacking'`                   |
| `{preferred_licenses}` or `{preferred_licenses[X]}`   | Preferred license types, where X can be set to a number to limit the results         | `'MIT','GPL'`                      |

#### Extended Text Variables (Raw GitHub API Data)

These variables are sourced directly from the GitHub User API data without any transformations, except for the reformatting of dates. Please note that this data may change over time, and the variables listed were the ones available at the time of writing:

| **Variable**                  | **Description**                            | **Example**                         |
| ----------------------------- | ------------------------------------------ | ----------------------------------- |
| `{login}`                     | GitHub login name                          | `'joanroig'`                        |
| `{id}`                        | Unique GitHub user ID                      | `'123456789'`                       |
| `{node_id}`                   | Node identifier                            | `'MDQ6VXNlcjEyMzQ1Njc4OQ=='`        |
| `{type}`                      | Type of account (e.g., "User")             | `'User'`                            |
| `{user_view_type}`            | User view type (e.g., "private")           | `'private'`                         |
| `{site_admin}`                | Site administrator status (Boolean)        | `'false'`                           |
| `{name}`                      | Display name                               | `'Joan Roig'`                       |
| `{company}`                   | Company name (if provided)                 | `'Company Inc.'`                    |
| `{blog}`                      | Blog URL                                   | `'https://blog.example.com'`        |
| `{location}`                  | User location                              | `'Barcelona, Spain'`                |
| `{email}`                     | Email address (if provided)                | `'joan@example.com'`                |
| `{hireable}`                  | Hireable status (if provided)              | `'true'`                            |
| `{bio}`                       | Biography                                  | `'Software developer and musician'` |
| `{twitter_username}`          | Twitter username                           | `'@joanroig'`                       |
| `{public_repos}`              | Count of public repositories               | `'35'`                              |
| `{public_gists}`              | Count of public gists                      | `'5'`                               |
| `{followers}`                 | Number of followers                        | `'200'`                             |
| `{following}`                 | Number of users followed                   | `'150'`                             |
| `{created_at}`                | Date the GitHub account was created        | `'2015-05-17'`                      |
| `{updated_at}`                | Date the GitHub account was last updated   | `'2025-04-05'`                      |
| `{private_gists}`             | Count of private gists                     | `'10'`                              |
| `{total_private_repos}`       | Total number of private repositories       | `'10'`                              |
| `{owned_private_repos}`       | Count of owned private repositories        | `'5'`                               |
| `{disk_usage}`                | Disk usage in kilobytes                    | `'50000'`                           |
| `{collaborators}`             | Number of collaborators                    | `'10'`                              |
| `{two_factor_authentication}` | Two-factor authentication status (Boolean) | `'true'`                            |

## Development Setup

### Requirements

- **Conda** or **Miniconda** (alternatively, only Python)
- **FFmpeg**
- **VSCode** (optional, for debugging and development)

### Setup

1. Clone this repository and open it in your IDE (e.g., **VSCode**).
2. Add your **PAT** token to the `.github_token` file.
3. If you have **Conda** installed, run `rebuild_env.ps1` to set up the Conda environment, then execute `run.ps1` to start the application. Otherwise, read the two scripts to run the commands using Python.
4. For debugging, use the provided **Run** and **Debug** configurations.

## Credits

Fonts by **VileR**: [Oldschool PC Fonts](https://int10h.org/oldschool-pc-fonts/fontlist/)

## License

This project is licensed under the [MIT License](LICENSE).
