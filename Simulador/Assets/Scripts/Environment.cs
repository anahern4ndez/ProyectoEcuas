using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Environment : MonoBehaviour {
    public GameObject edif2;
    public GameObject edif3;
    public GameObject edif4;
    public bool moviendo = false;
    private Vector3 posGameObject;

    // Use this for initialization
    void Start () {
        posGameObject = this.gameObject.transform.position; 
        StartCoroutine("CorutinaUpdatePos");

    }
	
	// Update is called once per frame
	void Update () {
		
	}
    IEnumerator CorutinaUpdatePos()
    {
        while (edif2.instance.moviendo)
        {
            yield return new WaitForSeconds(0.1f);
            //posicion del suelo 
            float posx = 
            //promedios de posiciones
            float corrimiento = (edif2.gameObject.transform.position.x + edif3.gameObject.transform.position.x + edif4.gameObject.transform.position.x)/3.0;
            this.gameObject.transform.position = new Vector3(this.gameObject.)
            hueso1.transform.position = new Vector3(hueso1pos.x + piso1x[contadorPos], hueso1pos.y, hueso1pos.z);
            hueso2.transform.position = new Vector3(hueso2pos.x + piso2x[contadorPos], hueso2pos.y, hueso2pos.z);
            hueso3.transform.position = new Vector3(hueso3pos.x + piso3x[contadorPos], hueso3pos.y, hueso3pos.z);
            contadorPos++;
        }
    }
}
