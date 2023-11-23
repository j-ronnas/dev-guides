# Guide: Spelarrörelse med rigidbody

### Rigidbody

En rigidbody i Unity är en *komponent* som man kan lägga till på ett objekt. Det objektet kan då interagera med fysiksystemet och agerar som ett fysiskt objekt med gravitation, kollisioner och krafter. För att lägga till en rigibody gör du följande:

1. Markera objektet i scen-vyn.
2. Scrolla längst ner i inspektorn
3. Tryck på knappen Add Component
4. Klicka dig fram eller sök efter rigidbody
5. Tryck på Rigidbody för ett 3D projekt och Rigidbody 2D för ett 2D-projekt


### Skapa egen komponent

För att skapa spelarrörelse vill vi lägga till en egen komponent som gör följande:

* Kolla om en knapp är nertryckt
* Lägg till en kraft åt en given riktning

*Exempel: om höger pil-tangent är nertryckt, lägg till en kraft åt höger*

Först behöver vi lägga till en komponent på objektet:

1. Markera objektet i scen-vyn.
2. Scrolla längst ner i inspektorn
3. Tryck på knappen Add Component
4. Skriv in namnet på den nya komponenten, till exempel: *PlayerMovement*
5. Tryck på new script
6. Kontrollera namnet, (det får inte ha mellanslag eller specialtecken) och tryck på *create and add*

Vi kan öppna skriptet genom komponenten, eller dubbelklicka på filen som har skapats i projektmappen.


### Styr rigidbody i kod

I vårt nya skript vill nu kunna styra vår rigidbody med kod. För att göra detta behöver vi skapa en variabel som representerar rigidbodyn. Vi skapar en Rigidbody-variabel på samma sätt som andra variabler, dvs `VariabelTyp variabelNamn`.

I unity-skriptet skriver vi alltså:

```csharp

public class PlayerMovement : MonoBehaviour
{
	Rigidbody myRigidbody;

	// Start is called before the first frame update
	void Start()
	{

	}

	// Update is called once per frame
	void Update()
	{

	}
}

```

Vi behöver också ge variabeln `myRigidbody` ett värde. Det gör vi i start-metoden, som kör en gång i början av spelet. Vi kan få tag på den rigidbody som finns på samma objekt med metoden `GetComponent<KomponentTyp>()`.

```csharp
	
	// Start is called before the first frame update
    void Start()
    {
    	myRigidbody = GetComponent<Rigidbody>();
    }

``` 

Nu har vi tillgång till rigidbodyn på objektet och vi anropa olika metoder på den. Framförallt vill vi använda en metod som heter `AddForce` för att applicera en kraft i en given riktning. 

```csharp
//Applicera en kraft på 20 Newton i x-led
myRigidbody.AddForce(new Vector3(20,0,0));
```

Så fort vi applicerar krafter och gör saker med fysisk systemet vill vi göra det i ´FixedUpdate´- metoden. Den körs ett fixt antal gånger per sekund (50 gånger per sekund), till skillnad från `Update` som kör så fort den kan.

Vi lägger till ett anrop till `AddForce` tillsammans med en if-sats som kollar om höger pil-tangent trycks ner i `FixedUpdate`

```csharp
void FixedUpdate()
{
	if(Input.GetKey(KeyCode.RightArrow)){
		myRigidbody.AddForce(new Vector3(20,0,0));
	}
}
```

Med detta kan vi nu få vår spelare att börja röra sig åt höger när man trycker på höger pil-tangent. Eventuellt kan man behöva justera hur stor kraft som appliceras genom att ändra vektorn vi anger som argument till `AddForce`.

På samma sätt kan vi styra åt vänster med en if-sats som kollar vänster pil-tanget och applicerar en kraft i negativt x-led.

```csharp
void FixedUpdate()
{
	if(Input.GetKey(KeyCode.RightArrow)){
		myRigidbody.AddForce(new Vector3(20,0,0));
	}

	if(Input.GetKey(KeyCode.LeftArrow)){
		myRigidbody.AddForce(new Vector3(-20,0,0));
	} 
}
```


### Extra