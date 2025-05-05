# BookBuddy

Η εφαρμογή που δημιουργήθηκε ονομάζεται BookBuddy. Είναι μια πλατφόρμα εύρεσης και ανταλλαγής βιβλίων χωρίς πληρωμή ή αγορά βιβλίων. Είναι μια διαδικτυακή πλατφόρμα που κάνει προσιτή και σύγχρονη την ανταλλαγή και τον δανεισμό βιβλίων μεταξυ των χρηστών της. 

Η εφαρμογή αυτή στοχεύει στην προώθηση της ανάγνωσης ως μορφή ψυχαγωγίας σε έναν κόσμο που η τεχνολογία τείνει να αποτελεί αντίπαλο του βιβλίου. Μέσω του BookBuddy o καθένας μπορεί να αναζητήσει, να προσφέρει ή να δανειστεί βιβλία χωρίς κόστος. 

Οι βασικοί χρήστες της πλατφόρμας είναι λάτρεις του βιβλίου, φοιτητές και κάτοικοι αστικών περιοχών, ανεξαρτήτως οικονομικής κατάστασης ή κοινωνικής τάξης. Είναι μια πλατφόρμα που προωθεί την κυκλική οικονομία και έχει φιλανθρωπικό και φιλικό προς το περιβάλλον χαρακτήρα. 

Απευθύνεται ακόμα σε άτομα που θέλουν να αποκτήσουν πρόσβαση σε πληθώρα τίτλων βιβλίων χωρίς να είναι αναγκασμένοι να αγοράσουν ή να ψάξουν κάποια κοντινή δανειστική βιβλιοθήκη. Η ανάγκη που καλύπτει η εφαρμογή αυτή ουσιαστικά είναι της ψυχαγωγίας μέσω της ανάγνωσης βιβλίων για ανθρώπους που δεν έχουν την οικονομική δυνατότητα να αγοράσουν νέα βιβλία ή υποστηρίζουν την ανακύκλωση βιβλίων και αντικειμένων και έχουν έντονη οικολογική συνείδηση. 

Η εφαρμογή παρέχει δυνατότητες αναζήτησης τίτλων, δυνατότητα καταχώρησης διαθέσιμων τίτλων προς δανεισμό, ανταλλαγής μηνυμάτων μεταξύ χρηστών και αξιολόγησης βιβλίων.

---

## Αναλυτική Περιγραφή και Τεκμηρίωση των Λειτουργιών

### Λειτουργία 1η: Συνδεση Χρήστη 

**Περιγραφή:**  
Ο  χρήστης συνδέεται στο λογαριασμό στο BookBuddy χρησιμοποιώντας το username και τον κωδικό του.

**Είσοδος:**  
Username και  password

**Έξοδος:**  
Ο χρήστης μεταφέρεται στην πλατφόρμα ως μέλος που μπορεί να στείλει μηνύματα και να ανεβάσει βιβλία.

**Mockup:**
![My example image](./mockups/login.png)

### Λειτουργία 2η: Αναζήτηση Τίτλων

**Περιγραφή:**  
Ο χρήστης έχει τη δυνατότητα να κάνει αναζήτηση για κάποιο βιβλίο που ψάχνει με βάση τον τίτλο του βιβλίου ή την κατηγορία του.

**Είσοδος:**  
Τίτλος Βιβλίου, Συγγραφέας, Καταχωρημένες Κατηγορίες

**Έξοδος:**  
Λίστα με αποτελέσματα βιβλίων που ταιριάζουν με τα κριτήρια αναζήτησης.

**Mockup:**
![My example image](./mockups/search_books.png)

---

### Λειτουργία 3η: Προβολή Λεπτομεριών Τίτλου Βιβλίου

**Περιγραφή:**  
Οι χρήστες μπορούν να δουν λέπτομερείες ,δηλαδή μια σχετικη περιγραφη του βιβλίου αλλά και σχολιασμούς άλλων χρηστών καθώς και στοιχεία για την κατάσταση του βιβλιου και του ιδιοκτήτη.

**Είσοδος:**  
Πάτημα στο κουμπί view details 

**Έξοδος:**  
Πλοήγη στο profile του τιτλου του βιβλίου.

**Mockup:**
![My example image](./mockups/book_details.png)

### Λειτουργία 4η: Αξιολόγηση Βιβλίου

**Περιγραφή:**  
Οι χρήστες μπορούν να αφήσουν αξιολόγηση του βιβλίου που διάβασαν.

**Είσοδος:**  
Αξιολόγηση 1–5 Αστέρια, Σχόλιο (προαιρετικά)

**Έξοδος:**  
Η αξιολόγηση καταγράφεται κάτω στα details του βιβλίου.

**Mockup:**
![My example image](./mockups/review.png)


### Λειτουργία 5η: Μηνύματα μεταξύ χρηστών

**Περιγραφή:**  
Οι εγγεγραμμένοι χρήστες μπορούν να ανταλλάξουν μηνύματα έτσι ώστε να βρουν τρόπο συνάντησης για την ανταλλαγή ή τον δανεισμό βιβλίου.

**Είσοδος:**  
Κλικ στο κουμπί "Contact Owner"

**Έξοδος:**  
Εμφανίζεται συνομιλία με τον ιδιοκτήτη του βιβλίου.


### Λειτουργία 6η: Εγγραφή Χρήστη 

**Περιγραφή:**  
Ο νέος χρήστης δημιουργεί λογαριασμό στο BookBuddy χρησιμοποιώντας το email του και δημιουργώντας ένα username και έναν κωδικό.

**Είσοδος:**  
Username, email, password

**Έξοδος:**  
Ο νέος χρήστης δημιουργεί λογαριασμό και μπορεί να ανεβάζει τα δικά του βιβλία , να σχολιάζει σε τίτλους και να ανταλλάσει μηνύματα.

**Mockup:**
![My example image](./mockups/register.png)

 
---



### Σχήμα Βάσης Δεδομένων
**Διευκρινήσεις:**  
Στο σχήμα φαινεταί το Profile το οποίο είναι υπο υλοποίηση. Είναι ενά συνολικο σχήμα για καλύτερη κατανόηση της τελικής λειτουργίας του site.

[Σχήμα βασης δεδομενων ](https://www.canva.com/design/DAGmfqO_faw/M2dPL7utAl4b7H8vTi8tNg/view?utm_content=DAGmfqO_faw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h5446adf6aa)


## Rename a file

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Delete a file

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

## Export a file

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# Synchronization

Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your **Google Drive**, your **Dropbox** and your **GitHub** accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow... The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.

There are two types of synchronization and they can complement each other:

- The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.
	> To start syncing your workspace, just sign in with Google in the menu.

- The file synchronization will keep one file of the workspace synced with one or multiple files in **Google Drive**, **Dropbox** or **GitHub**.
	> Before starting to sync files, you must link an account in the **Synchronize** sub-menu.

## Open a file

You can open a file from **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Open from**. Once opened in the workspace, any modification in the file will be automatically synced.

## Save a file

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Synchronize a file

Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.

If you just have modified your file and you want to force syncing, click the **Synchronize now** button in the navigation bar.

> **Note:** The **Synchronize now** button is disabled if you have no file to synchronize.

## Manage file synchronization

Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking **File synchronization** in the **Synchronize** sub-menu. This allows you to list and remove synchronized locations that are linked to your file.


# Publication

Publishing in StackEdit makes it simple for you to publish online your files. Once you're happy with a file, you can publish it to different hosting platforms like **Blogger**, **Dropbox**, **Gist**, **GitHub**, **Google Drive**, **WordPress** and **Zendesk**. With [Handlebars templates](http://handlebarsjs.com/), you have full control over what you export.

> Before starting to publish, you must link an account in the **Publish** sub-menu.

## Publish a File

You can publish your file by opening the **Publish** sub-menu and by clicking **Publish to**. For some locations, you can choose between the following formats:

- Markdown: publish the Markdown text on a website that can interpret it (**GitHub** for instance),
- HTML: publish the file converted to HTML via a Handlebars template (on a blog for example).

## Update a publication

After publishing, StackEdit keeps your file linked to that publication which makes it easy for you to re-publish it. Once you have modified your file and you want to update your publication, click on the **Publish now** button in the navigation bar.

> **Note:** The **Publish now** button is disabled if your file has not been published yet.

## Manage file publication

Since one file can be published to multiple locations, you can list and manage publish locations by clicking **File publication** in the **Publish** sub-menu. This allows you to list and remove publication locations that are linked to your file.


# Markdown extensions

StackEdit extends the standard Markdown syntax by adding extra **Markdown extensions**, providing you with some nice features.

> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```