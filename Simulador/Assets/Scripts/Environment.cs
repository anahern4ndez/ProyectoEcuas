using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Environment : MonoBehaviour {
    float[] piso1x;
    public bool moviendo = false;
    private Vector3 posGameObject;
    private float corrimiento;
    int contadorPos = 0;
    private int N; //cantidad de datos
    // Use this for initialization
    void Start () {

        string[] lines = System.IO.File.ReadAllLines("Assets/Py/four_floors.dat");
        N = lines.Length;
        piso1x = new float[lines.Length]; 
        int i = 0;
        foreach (string line in lines)
        {
            // Use a tab to indent each line of the file.
            string[] sep;
            sep = line.Split();
            piso1x[i] = float.Parse(sep[1]);
            i++;
        }
        posGameObject = this.gameObject.transform.position; 
        StartCoroutine("CorutinaUpdatePos");

    }
	
	// Update is called once per frame
	void Update () {
		
	}
    IEnumerator CorutinaUpdatePos()
    {
        while (contadorPos < N)
        {
            yield return new WaitForSeconds(0.1f);
            this.gameObject.transform.position = new Vector3(this.gameObject.transform.position.x +(piso1x[contadorPos]/10f), this.gameObject.transform.position.y, this.gameObject.transform.position.z);
            contadorPos++;
        }
    }
}
