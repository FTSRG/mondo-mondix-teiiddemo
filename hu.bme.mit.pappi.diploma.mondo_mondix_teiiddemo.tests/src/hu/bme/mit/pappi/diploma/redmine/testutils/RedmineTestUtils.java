package hu.bme.mit.pappi.diploma.redmine.testutils;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;

public class RedmineTestUtils {

	private final static String BASE_URL = "http://redmine:3000";
	private static String loginname = "userToDelete";
	public final static String ADMIN_USER = "admin";
	public final static String ADMIN_PASS = "admin";

	public static void addTestUserToRedmine() {
		WebDriver driver = doLogin(ADMIN_USER, ADMIN_PASS);
		
		driver.findElement(By.xpath("//a[contains(@href, '/admin')]")).click();
		driver.findElement(
				By.xpath("//div[@id='admin-menu']/ul/li[2]/a")).click();
		driver.findElement(By.xpath("//div[@id='content']/div/a"))
				.click();
		
		driver.findElement(By.id("user_login")).clear();
		driver.findElement(By.id("user_login")).sendKeys(loginname);

		driver.findElement(By.id("user_firstname")).clear();
		driver.findElement(By.id("user_firstname")).sendKeys(loginname);

		driver.findElement(By.id("user_lastname")).clear();
		driver.findElement(By.id("user_lastname")).sendKeys(loginname);

		driver.findElement(By.id("user_mail")).clear();
		driver.findElement(By.id("user_mail")).sendKeys("test@test.hu");

		driver.findElement(By.id("user_password")).clear();
		driver.findElement(By.id("user_password")).sendKeys(loginname);

		driver.findElement(By.id("user_password_confirmation")).clear();
		driver.findElement(By.id("user_password_confirmation")).sendKeys(loginname);

		driver.findElement(By.xpath("//form[@id='new_user']/p/input[2]"))
				.click();
		
	}
	
	public static void removeTestUserFromRedmine() {
		
	}
	
	public static WebDriver doLogin(String username, String password) {

		//WebDriver driver = new FirefoxDriver();
		WebDriver driver = new HtmlUnitDriver();

		driver.get(BASE_URL + "/login");

		driver.findElement(By.xpath("//a[contains(@href, '/login')]")).click();
		driver.findElement(By.id("username")).clear();
		driver.findElement(By.id("username")).sendKeys(username);
		driver.findElement(By.id("password")).clear();
		driver.findElement(By.id("password")).sendKeys(password);
		driver.findElement(By.xpath("//div[@id='login-form']/form/table/tbody/tr[4]/td[2]/input")).click();
		
		System.out.println("Logged in as " + username);
		return driver;
	}
}
