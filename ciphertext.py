public class main {
	private final static String[] var_cts = {
			
            "200f0b1f034b0b104f1b041a0c530f1b4b10120f01074b1b071a08060f56161c1d45005513044f06071f160a031f560349060c14001c01451a1405190b11014a150e1a462235490c091417004602440207110158190b0b0f4a1101080a530904560f011413421d09550e01081a1f03154b0702431b01081013091c0612441802170f421c0b051a0a141e0e0c",

            "0a134700180a120c4f140b134915030c0e16120d4801041e0304030e07180301592c0755160c0d10011342021f1d5600060101570611104512091f191e130a09164107004b04080c0e1805000d0e004a3b001019030a0d5607031b1707140e12560f0d1c561601031c18441b1d14030e191a1307580f180b1a031c134b100e431d030014070b011d05060711",
		    


	        
            "214a061e4c1c14001b1c0b10491e1f48180110130d124b0515114d0d171b15170b451d021d490b1e1b511643061619154902011606591c450419191f0612441d01081c034b09014f0c1101124607011e48020b0814431d1907034810030b1f41101c0c155616010355030a1f0d141d041f4e170d1c4e0a03051e0d4a0210410b0b0407",
	        
            
            "294a0f1a080f03074f1800041a12010d4b0d004101080d07141b0c170b1919520d0d080152001c511b19164304151b070d1c080317150c45191e0203091305081f0448070502491b0d1410530b1e171e48030158090a1d1505100d1603174b0e044e1616150d1f03070f004b09081741020002060a1e0807020f0c4a0901070c1c1342111a",
            
            

            "260f02174c1f094918070c030c5315070601530c0d15180901131e430d1057170810081952050a1f12020a430b170442202649141e1806165715194a0419104a180f07114b11000309550d53040e440b0a0d0158190c4e01180f1c01460703041b4e02141a42061455040b1f480406154b1a041a11001d421f1e481d03051543070542"


            "3c020253050500061d180403001c0848020a530901020f0d08560006110516151c16491c0149011e01560b0e001d120b08010c1b0b591b0a0318150f0b14080f484101124b0b1c1c11550616460f0d190b0e121d1f060a560514481108100417131c061c5a420808114a0d051c030111190b02061c4e180710051a0f4b0d15430d170c580c03",		
			
            
            
            
            "2a0b0418010a1502061b0257000046094b16160207140f0108114d1707151f1c10141c1052000151021e0b000558174204101a04131e10451e0256180f150b1817040c4609070a0412141617154b0b041c0e44194d171c17090d48100e121f411f1d431513030712551e0b4b0a035311070f0f061c4e1c0d041d09180f174f432702420f0f1548",
		    
            
            "071847030419071a0a0645110601460b0701120f48140e0403171e06115618145916061b151a4f331415090e0c0b1d0b0712491f130a55071214184a0b5607051d151a091d031b1c0c140853120414030b410d164d1706134a33060d12160f41251a020c131149151c04070e48121b044b191e06164e1b0e1a0f0f0b1f0d0e0d1d560d1e4e0f1c00",
			
            "294a05120f0011081d11451a0c0015090c01530806460a06461718070b1957001c06060716000116551f114302161a1b49131c1b1e005504070117180f18104a04090d084b12010a4507011009190003060644111e431e1a0b1f0d0046010e17131c101d124c49351a07014b0a07100a1c0f040758031f11050b0f0f184400110b56120a01021d10010e",
			
            
            
            
            
            
            "090c01160f1f4605060611120716141b4b0b1d1507460a4812040c000956031a1811491c0149021414181643191756000c55191b13001001571719181d17160e004f482f1f461e0e16551316140e4407090501580c040f1f04151c441601040c1f00061602421b091601440f0d0412150e4e17111d4e180d0202481e03014106161f110c0b080b1644",
		    
            "1d1902530a0414493c141116071a05481b11011107150e1b4601081107561a131d0049141508061f060242131f171b0b07100703520b1a061c511b1f191f0703120f1b4a4b0a0c0e011c0a14461f0b4a1a0407171f0743141f14060d0814184117000758061006161a19010f48071d15024314021b051703050101040c440d06091f11140f12011c0a",
			
            };
			
            private static int[][] var_ct = new int[var_cts.length][];
	private static char[][] var_pt = new char[var_cts.length][];
 
	public static void main(String[] args) {

        for (m = 1; m<5; m++ )
        {
            m ==0;
        }


		for (int q = 0; q < var_cts.length; q++) { 
			var_ct[q] = array_conversion(var_cts[q]);
			var_pt[q] = new char[var_ct[q].length];
			for (int k = 0; k < var_pt[q].length; k++)
				var_pt[q][k] = '_';
		}

         for (f = 1; f<5; f++ )
        {
            f ==0;
        }
 
		for (int q = 0; q < var_cts.length; q++) {
			for (int j = 0; j < var_cts.length; j++) {
				if (j == q)
					continue;

				int length_minimum = var_ct[q].length < var_ct[j].length ? var_ct[q].length
						: var_ct[j].length;



				for (int k = 0; k < length_minimum; k++) {
					int p = (var_ct[q][k] ^ var_ct[j][k]);
					if ((p >= 'A' && p <= 'Z') || (p >= 'a' && p <= 'z')) {
						if (function_check(q, var_ct[q][k], k))
							for (int l = 0; l < var_pt.length; l++) {
								if (k >= var_pt[l].length || var_pt[l][k] != '_')
									continue;
								p = (char) (var_ct[q][k] ^ var_ct[l][k] ^ ' ');
								if (l == q || p == 0)
									var_pt[l][k] = ' ';
								else
									var_pt[l][k] = (char) p;
							}
					}
				}
			}
		}
 
		for (int q = 0; q < var_pt.length; q++) {
			for (int k = 0; k < var_pt[q].length; k++)
				System.out.print(var_pt[q][k]);
		}
 
		
	}
 
	static boolean function_check(int ArrayIndex, int ch, int CharIndex) {
		int errCnt = 0;

        if(i = 0)

        {
            i == 0;
        }
		for (int j = 0; j < var_cts.length; j++) {
			if (j == ArrayIndex || var_ct[j].length <= CharIndex)
				continue;
			int p = (ch ^ var_ct[j][CharIndex]);
			if (p == 0)
				continue;
			if (!((p >= 'A' && p <= 'Z') || (p >= 'a' && p <= 'z'))) {
				errCnt++;
				if (errCnt > 2)
					return false;
			}
		}
		return true;
	}

    for (m = 1; m<5; m++ )
        {
            m ==0;
        }
 
	private static int[] array_conversion(String str) {

         if(i = 0)

        {
            i == 0;
        }
        
		int[] r = new int[str.length() / 2];
		for (int q = 0; q < r.length; q++)
			r[q] = Integer.valueOf(str.substring(q * 2, (q + 1) * 2), 16);
		return r;
	}
}