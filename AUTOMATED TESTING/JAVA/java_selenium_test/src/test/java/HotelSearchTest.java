import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.Assert;
import org.testng.annotations.Test;
import java.util.List;
import java.util.stream.Collectors;

public class HotelSearchTest extends BaseTest {


    @Test
    public void searchHotelTest() {
        driver.findElement(By.xpath("//span[text()='Search by Hotel or City Name']")).click();
        driver.findElement(By.xpath("//div[@id='select2-drop']//input")).sendKeys("Dubai");
        driver.findElement(By.xpath("//span[@class='select2-match' and text()='Dubai']")).click();
        driver.findElement(By.name("checkin")).sendKeys("24/12/2023");
        driver.findElement(By.name("checkout")).sendKeys("30/12/2023");
        driver.findElement(By.id("travellersInput")).click();
        driver.findElement(By.id("adultPlusBtn")).click();
        driver.findElement(By.id("childPlusBtn")).click();
        driver.findElement(By.xpath("//button[text()=' Search']")).click();

        List<String> hotelNames = driver.findElements(By.xpath("//h4[contains(@class,'list_title')]//b"))
                .stream().map(el -> el.getAttribute("textContent")).collect(Collectors.toList());

        Assert.assertEquals(hotelNames.get(0), "Jumeirah Beach Hotel");
        Assert.assertEquals(hotelNames.get(1), "Oasis Beach Tower");
        Assert.assertEquals(hotelNames.get(2), "Rose Rayhaan Rotana");
        Assert.assertEquals(hotelNames.get(3), "Hyatt Regency Perth");

    }
        @Test
        public void searchHotelWithoutNameTest() {

            driver.findElement(By.name("checkin")).sendKeys("06/12/2023");
            driver.findElement(By.name("checkout")).sendKeys("13/12/2023");
            driver.findElement(By.id("travellersInput")).click();
            driver.findElement(By.id("adultPlusBtn")).click();
            driver.findElement(By.id("childPlusBtn")).click();
            driver.findElement(By.id("childPlusBtn")).click();

            driver.findElement(By.xpath("//button[text()=' Search']")).click();
            WebElement noResultHeading = driver.findElement(By.xpath("//h2[@class = 'text-center']"));
            Assert.assertTrue(noResultHeading.isDisplayed());
            Assert.assertEquals(noResultHeading.getText(), "No Results Found");


    }
}
