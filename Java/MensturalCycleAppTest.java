import org.junit.jupiter.api.Test;
import java.time.LocalDate;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class MensturalCycleAppTest{
@Test
	public void testForDateFunctionality() {
	
	int monthNumber = 10;
	int dayNumber = 15;
	
     MensturalCycleApp input = new MensturalCycleApp();
	String result = input.dateCollection(monthNumber, dayNumber);
	
	assertEquals(result, "2025-10-15");
	}

  }   